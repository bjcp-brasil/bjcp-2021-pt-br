#!/usr/bin/env python3
"""Gera bjcp-2021-pt-br.json a partir dos .tex deste repositório, no mesmo
schema do bjcp-2021.json em inglês distribuído em
https://github.com/bjcp-brasil/styleguide-2021.

Requer Docker (usa a mesma imagem pandoc/core:2.9 do pipeline do site).

Uso:
    python3 tools/styleguide-dataset/build_dataset.py
    python3 tools/styleguide-dataset/convert_formats.py   # gera .xml/.yaml

Depois, copie os 3 arquivos gerados (bjcp-2021-pt-br.json/.xml/.yaml) pra
raiz de bjcp-brasil/styleguide-2021 e commit lá — este script não escreve
direto no outro repositório.
"""
import json
import os
import re
import subprocess

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
OUT = os.path.join(os.path.dirname(__file__), "bjcp-2021-pt-br.json")

FIELD_LABELS = {
    "impression": ["Impressão Geral", "Impressões Gerais", "Impressão geral"],
    "aroma": ["Aroma"],
    "appearance": ["Aparência"],
    "flavor": ["Sabor"],
    "mouthfeel": ["Sensação na Boca", "Sensações de Boca"],
    "comments": ["Comentários"],
    "history": ["História"],
    "ingredients": ["Ingredientes", "Ingredientes Caraterísticos"],
    "comparison": ["Comparação de Estilos", "Comparação de estilos"],
}
EXAMPLES_LABELS = ["Exemplos Comerciais"]
TAGS_LABELS = ["Atributos de Estilo", "Atributos de Estilos"]


def read(relpath):
    with open(os.path.join(REPO, relpath), encoding="utf-8") as f:
        return f.read()


def extract_inputs(relpath):
    return re.findall(r"\\input\{([^}]+)\}", read(relpath))


def pandoc_md(relpath):
    result = subprocess.run(
        [
            "docker", "run", "--rm",
            "-v", f"{REPO}:/data", "-w", "/data",
            "pandoc/core:2.9",
            "-f", "latex", "-t", "gfm",
            relpath,
        ],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"pandoc falhou em {relpath}: {result.stderr}")
    return result.stdout


def clean_text(text):
    text = text.strip()
    text = re.sub(r"\s*\n\s*", " ", text)  # pandoc quebra linha em ~80 col
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # [texto](link) -> texto
    text = text.replace("**", "").replace("*", "")
    text = re.sub(r" {2,}", " ", text)
    return text.strip()


def find_field(md, labels):
    for label in labels:
        pattern = (
            r"\*\*" + re.escape(label) + r"\*\*:\s*(.*?)"
            r"(?=\n\n\*\*[A-ZÀ-Ú]|\n\n\||\Z)"
        )
        m = re.search(pattern, md, re.S)
        if m:
            return clean_text(m.group(1))
    return None


def find_list_field(md, labels):
    text = find_field(md, labels)
    if not text:
        return None
    text = text.rstrip(".").strip()
    items = [x.strip() for x in text.split(",") if x.strip()]
    return items or None


def find_stats(md):
    stats = {}
    for json_key, tex_key in [
        ("og", "OG"), ("ibus", "IBU"), ("fg", "FG"), ("srm", "SRM"), ("abv", "ABV"),
    ]:
        m = re.search(
            re.escape(tex_key) + r":\s*([\d.,]+)\s*%?\s*[-–]\s*([\d.,]+)\s*%?",
            md,
        )
        if m:
            stats[json_key] = {
                "min": m.group(1).replace(",", "."),
                "max": m.group(2).replace(",", "."),
            }
    if stats:
        return stats
    # Categorias abertas/especiais (ex.: Fruit Beer, Wood Beer, Experimental
    # Beer) não têm faixa numérica fixa -- o campo é texto livre tipo "Varia
    # com o estilo base.". Mesmo padrão do JSON em inglês pra casos
    # equivalentes (ver "21B Specialty IPA": {"statistics": {"notes": "..."}}).
    notes = find_field(md, ["Estatísticas"])
    if notes:
        return {"notes": notes}
    return None


def parse_id_name(heading):
    # pandoc escapa "N." no início de linha como "N\." pra não virar lista
    # ordenada em markdown.
    heading = heading.strip().replace("\\.", ".")
    m = re.match(r"([0-9]+[A-Z]?|X[0-9]+)\.\s*(.+)", heading)
    if m:
        return m.group(1), m.group(2).strip()
    return "", heading.strip()


def get_heading(md):
    m = re.search(r"^#{1,2} (.+)$", md, re.M)
    return m.group(1).strip() if m else ""


def parse_style(relpath):
    md = pandoc_md(relpath)
    heading = get_heading(md)
    style_id, style_name = parse_id_name(heading)

    sub = {"id": style_id, "name": style_name}
    for key, labels in FIELD_LABELS.items():
        val = find_field(md, labels)
        if val:
            sub[key] = val

    stats = find_stats(md)
    if stats:
        sub["statistics"] = stats

    examples = find_list_field(md, EXAMPLES_LABELS)
    if examples:
        sub["examples"] = examples

    tags = find_list_field(md, TAGS_LABELS)
    if tags:
        sub["tags"] = tags

    return sub


def parse_category_notes(header_relpath):
    md = pandoc_md(header_relpath)
    heading = get_heading(md)
    cat_id, cat_name = parse_id_name(heading)
    body = re.sub(r"^#{1,2} .+\n+", "", md, count=1)
    notes = clean_text(body)
    return cat_id, cat_name, notes


def build_category(dir_):
    header_rel = f"{dir_}/header.tex"
    index_rel = f"{dir_}/index.tex"
    cat_id, cat_name, notes = parse_category_notes(header_rel)

    files = [
        os.path.basename(p)
        for p in extract_inputs(index_rel)
        if os.path.basename(p) != "header.tex"
    ]
    subs = []
    for fname in files:
        print(f"  [estilo] {dir_}/{fname}")
        subs.append(parse_style(f"{dir_}/{fname}"))

    return {"id": cat_id, "name": cat_name, "notes": notes, "subcategory": subs}


def build_provisional(appendix_relpath):
    content = read(appendix_relpath)
    nested = re.findall(r"\\input\{([^}]+)\}", content)
    subs = []
    for rel in nested:
        print(f"  [estilo provisório] {rel}")
        subs.append(parse_style(rel))
    return {"id": "Estilos Provisórios", "name": None, "notes": "Estilos Provisórios", "subcategory": subs}


def main():
    main_inputs = [p for p in extract_inputs("main.tex") if p != "frontpage.tex"]

    categories = []
    for entry in main_inputs:
        if entry.endswith("/index.tex"):
            dir_ = entry[: -len("/index.tex")]
            if dir_.startswith("introducao"):
                # Seções de introdução do guia (não são categorias de
                # estilo julgáveis -- glossário, como usar o guia, etc.)
                # não têm equivalente no schema styleguide em inglês.
                print(f"[ignorado, introdução] {dir_}")
                continue
            print(f"[categoria] {dir_}")
            categories.append(build_category(dir_))
        elif entry.startswith("appendix/"):
            # appendix/a-appendix.tex (categorizações alternativas, não é
            # dado de "estilo") é ignorado de propósito -- não tem
            # equivalente no schema styleguide (sem campos de estilo).
            # appendix/b-appendix.tex (estilos regionais/provisórios) vira
            # a pseudo-categoria "Estilos Provisórios", igual ao "Provisional
            # Styles" do JSON em inglês.
            nested = re.findall(r"\\input\{([^}]+)\}", read(entry))
            if nested:
                print(f"[provisórios] {entry}")
                categories.append(build_provisional(entry))
            else:
                print(f"[ignorado, sem estilos] {entry}")

    result = {
        "styleguide": {
            "version": "2021",
            "revision": "2",
            "category": categories,
        }
    }

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    total_subs = sum(len(c["subcategory"]) for c in categories)
    print(f"\nPronto: {len(categories)} categorias, {total_subs} subcategorias -> {OUT}")


if __name__ == "__main__":
    main()
