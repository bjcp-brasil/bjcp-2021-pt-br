#!/usr/bin/env python3
"""Regenerates PHRASE_BANK.md.

The BJCP style guide reuses a lot of boilerplate sentences across styles
(e.g. "The entrant must specify the type(s) of fruit used."). Different
translators working on different pages can end up phrasing the same English
sentence differently in PT-BR. This script finds those repeated English
sentences and, where a page containing that sentence has already been
translated, pulls out the PT-BR wording that was used for it as a
"canonical" suggestion.

Source of the English reference text: scripts/bjcp-2021-en.json, vendored
from bjcp-brasil/styleguide-2021 (commit 251623b, 2026-07-10) -- a
structured English parse of the official 2021 BJCP Style Guidelines,
maintained by this same GitHub org. Unlike the sibling projects
cider-guidelines-2025-pt-br / mead-guidelines-2026-pt-br (which anchor on a
GENESIS_COMMIT in their own git history, since English text lived in-repo
before translation started), this repo's history has no such commit -- the
PT-BR text was already present in the very first commit for every style --
so it anchors on that external EN dataset instead. Re-vendor
scripts/bjcp-2021-en.json only if BJCP revises the 2021 guidelines text;
don't re-fetch casually, since a spurious diff there would look like a
translation change on every page that touches it.

The current PT-BR text is NOT vendored -- it's regenerated fresh on every
run by tools/styleguide-dataset/build_dataset.py (requires Docker; see that
script's docstring), so this always reflects the latest .tex content, never
a stale snapshot.

Usage:
    python3 scripts/generate-phrase-bank.py > PHRASE_BANK.md

Re-run this after translating or revising a page, so newly-established
wording feeds back into the bank for the next translator to match.

phrase-bank-overrides.json (same directory as this script) holds canonical
PT-BR wording agreed on *before* any page containing that sentence has been
translated yet -- e.g. someone pre-translates a batch of glossary phrases
ahead of actually translating the pages. Never hand-edit PHRASE_BANK.md to
add these; add them here instead, so a regeneration doesn't silently drop
them (PHRASE_BANK.md is always generated, never hand-edited). Once a real
page translates one of these sentences, its wording is compared against the
override like any other source -- a mismatch shows up as a normal
divergence to resolve (pick one, update the other).

Adapted from the sibling projects bjcp-brasil/cider-guidelines-2025-pt-br
and bjcp-brasil/mead-guidelines-2026-pt-br, which use the same convention
but anchor on an in-repo GENESIS_COMMIT instead of an external dataset.
"""
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
EN_JSON_PATH = Path(__file__).parent / "bjcp-2021-en.json"
BUILD_DATASET_SCRIPT = REPO_ROOT / "tools" / "styleguide-dataset" / "build_dataset.py"
PT_JSON_PATH = REPO_ROOT / "tools" / "styleguide-dataset" / "bjcp-2021-pt-br.json"
OVERRIDES_PATH = Path(__file__).parent / "phrase-bank-overrides.json"
PREDEFINED_SOURCE = "predefined"

MIN_OCCURRENCES = 2
MIN_SENTENCE_LEN = 20

# JSON field key -> friendly PT-BR label, used only for the rendered table's
# "Campo" hint on divergences. Order doesn't matter, this isn't the field
# list to iterate (see FIELDS below) -- "impression" intentionally excluded
# from a couple of provisional-style entries etc. is handled by "field
# missing on either side -> skip", not by this dict.
FIELD_LABEL_PT = {
    "impression": "Impressão Geral",
    "aroma": "Aroma",
    "appearance": "Aparência",
    "flavor": "Sabor",
    "mouthfeel": "Sensação na Boca",
    "comments": "Comentários",
    "history": "História",
    "ingredients": "Ingredientes",
    "comparison": "Comparação de Estilos",
    "entryinstructions": "Instruções para Inscrição",
    "notes": "(preâmbulo da categoria)",
}
FIELDS = [k for k in FIELD_LABEL_PT if k != "notes"]

# The EN dataset's pseudo-category for regional/experimental styles is
# named "Provisional Styles" (id used as a key, not a real BJCP category
# number); this repo's dataset builder names the same thing "Estilos
# Provisórios". Subcategory ids underneath (X1..X5) already match directly.
CATEGORY_ID_PT_TO_EN = {"Estilos Provisórios": "Provisional Styles"}


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))["styleguide"]


def build_pt_dataset():
    print("Gerando dataset PT-BR atual (tools/styleguide-dataset/build_dataset.py)...", file=sys.stderr)
    subprocess.run([sys.executable, str(BUILD_DATASET_SCRIPT)], check=True, cwd=REPO_ROOT,
                    stdout=subprocess.DEVNULL)
    return load_json(PT_JSON_PATH)


def index_dataset(styleguide, id_remap=None):
    """Flattens a styleguide dict into {(kind, id, field): text}.

    kind is "sub" for a subcategory field or "cat" for a category's notes
    (preamble) paragraph. id_remap translates this dataset's category ids
    to the other dataset's, so the two can be joined on the same key.
    """
    id_remap = id_remap or {}
    blocks = {}
    for cat in styleguide["category"]:
        cat_id = id_remap.get(cat["id"], cat["id"])
        if cat.get("notes"):
            blocks[("cat", cat_id, "notes")] = cat["notes"]
        for sub in cat.get("subcategory") or []:
            for field in FIELDS:
                val = sub.get(field)
                if val:
                    blocks[("sub", sub["id"], field)] = val
    return blocks


def code_for(kind, block_id):
    if kind == "cat":
        return f"Cat {block_id}" if block_id != "Provisional Styles" else "Cat. Estilos Provisórios"
    return block_id


def clean_text(s):
    s = re.sub(r"[‘’]", "'", s)
    s = re.sub(r"[“”]", '"', s)
    return re.sub(r"\s+", " ", s).strip()


def split_sentences(s):
    s = clean_text(s)
    protected = re.sub(
        r"\b(e\.g|i\.e|etc|vs|Mr|Mrs|Sr|Sra|No)\.",
        lambda m: m.group(0).replace(".", "<DOT>"),
        s,
    )
    parts = re.split(r"(?<=[.!?])\s+(?=[A-ZÁÀÂÃÉÍÓÔÕÚÇ(])", protected)
    parts = [p.replace("<DOT>", ".").strip() for p in parts]
    return [p for p in parts if len(p) >= MIN_SENTENCE_LEN]


def norm_key(sent):
    key = re.sub(r"[-–—]+", "-", sent)
    return clean_text(key).lower()


def build_repeated_sentence_index(en_blocks):
    locations = defaultdict(list)
    for (kind, block_id, field), text in en_blocks.items():
        code = code_for(kind, block_id)
        for sent in split_sentences(text):
            locations[norm_key(sent)].append((code, sent, field))
    return {k: v for k, v in locations.items() if len(v) >= MIN_OCCURRENCES}


def build_pt_variants(en_blocks, pt_blocks):
    """Best-effort EN->PT sentence alignment for already-translated blocks.

    Aligns by (kind, id, field) block, then by sentence position within the
    block. Skips any block where the EN/PT sentence counts don't match,
    since that means the translation merged/split sentences and positional
    alignment would silently pair the wrong sentences.

    Returns key -> list of (pt_sentence, code), keeping every variant seen
    (not just one) so divergent translations of the same EN sentence can be
    detected instead of silently overwritten.
    """
    variants = defaultdict(list)
    for key_id, en_text in en_blocks.items():
        pt_text = pt_blocks.get(key_id)
        if not pt_text:
            continue  # page not translated yet, or field missing on this side
        kind, block_id, field = key_id
        o_sents = split_sentences(en_text)
        c_sents = split_sentences(pt_text)
        if len(o_sents) != len(c_sents) or not o_sents:
            continue
        code = code_for(kind, block_id)
        for o, c in zip(o_sents, c_sents):
            key = norm_key(o)
            if key == norm_key(c):
                continue  # would only happen if PT text equals EN verbatim
            variants[key].append((c, code))

    if OVERRIDES_PATH.exists():
        overrides = json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))
        for en, pt in overrides.items():
            variants[norm_key(en)].append((pt, PREDEFINED_SOURCE))

    return variants


def pick_canonical(variant_list):
    """Picks the most-used distinct PT wording (ties: first seen) as canonical."""
    counts = defaultdict(int)
    first_seen = {}
    for pt, _ in variant_list:
        k = norm_key(pt)
        counts[k] += 1
        first_seen.setdefault(k, pt)
    best_key = max(counts, key=lambda k: (counts[k], -list(first_seen).index(k)))
    return first_seen[best_key]


def find_divergences(variants):
    """key -> {pt_wording: [codes]} for EN sentences translated >1 distinct way."""
    divergences = {}
    for key, occ in variants.items():
        by_wording = defaultdict(list)
        for pt, code in occ:
            by_wording[norm_key(pt)].append((pt, code))
        if len(by_wording) > 1:
            divergences[key] = {
                group[0][0]: [c for _, c in group]
                for group in by_wording.values()
            }
    return divergences


def render_markdown(repeated, variants, divergences):
    alignment = {k: pick_canonical(v) for k, v in variants.items()}
    items = sorted(repeated.items(), key=lambda kv: -len(kv[1]))
    matched = sum(1 for k in repeated if k in alignment)

    lines = []
    lines.append("# Banco de frases repetidas")
    lines.append("")
    lines.append(
        "O guia original em inglês repete muitas frases padronizadas entre "
        "estilos (ex.: \"The entrant must specify the type(s) of fruit "
        "used.\"). Esta lista existe pra garantir que, ainda que traduzidas "
        "por pessoas diferentes, essas frases fiquem com a mesma redação em "
        "PT-BR."
    )
    lines.append("")
    lines.append(
        f"Gerado por [`scripts/generate-phrase-bank.py`](scripts/generate-phrase-bank.py) "
        f"a partir do texto original em inglês vendorizado em "
        f"[`scripts/bjcp-2021-en.json`](scripts/bjcp-2021-en.json) (dataset "
        f"estruturado do Guia de Estilos 2021 do BJCP, via "
        f"[bjcp-brasil/styleguide-2021](https://github.com/bjcp-brasil/styleguide-2021)) "
        f"comparado com o texto PT-BR atual das páginas `.tex` deste repositório "
        f"(regenerado a cada execução por "
        f"[`tools/styleguide-dataset/build_dataset.py`](tools/styleguide-dataset/build_dataset.py)). "
        f"Considera frases com {MIN_OCCURRENCES}+ ocorrências idênticas no "
        f"original em inglês (comparação exata, após normalizar espaços/aspas/"
        f"travessão) — variações de redação da mesma ideia não são detectadas "
        f"automaticamente."
    )
    lines.append("")
    lines.append(
        f"**{len(items)} frases repetidas** encontradas, cobrindo "
        f"{sum(len(v) for v in repeated.values())} ocorrências no total. "
        f"**{matched}/{len(items)}** já têm uma tradução canônica sugerida — extraída "
        f"de páginas já traduzidas ou, quando marcado \"pré-definido\", combinada antes "
        f"de qualquer página ter traduzido a frase (ver "
        f"[`scripts/phrase-bank-overrides.json`](scripts/phrase-bank-overrides.json))."
    )
    lines.append("")
    lines.append("## Como usar")
    lines.append("")
    lines.append(
        "- Traduzindo ou revisando uma página: se uma frase dela aparece nesta "
        "lista **com** tradução canônica preenchida, use essa mesma redação."
    )
    lines.append(
        "- Se aparece na lista **sem** tradução canônica (coluna vazia), essa é a "
        "primeira vez que a frase está sendo traduzida — escolha a redação e, "
        "depois, rode o script de novo pra ela entrar como canônica pras próximas "
        "ocorrências."
    )
    lines.append(
        "- Depois de traduzir/revisar uma página, regenere este arquivo: "
        "`python3 scripts/generate-phrase-bank.py > PHRASE_BANK.md` (precisa de "
        "Docker rodando, usado pelo `build_dataset.py`)."
    )
    lines.append("")

    if divergences:
        lines.append(
            f"## ⚠️ {len(divergences)} divergência(s) encontrada(s)"
        )
        lines.append("")
        lines.append(
            "A mesma frase em inglês foi traduzida de mais de um jeito em páginas "
            "diferentes. Escolha uma redação e corrija as demais páginas pra "
            "convergir."
        )
        lines.append("")
        for key, by_wording in divergences.items():
            en_example = repeated[key][0][1] if key in repeated else key
            lines.append(f"- EN: {en_example}")
            for pt_text, codes in by_wording.items():
                pages = ", ".join(sorted(set(codes), key=lambda c: (len(c), c)))
                lines.append(f"  - \"{pt_text}\" — {pages}")
        lines.append("")
    else:
        lines.append(
            "## ✅ Nenhuma divergência encontrada\n\n"
            "Nenhuma frase repetida com tradução conhecida está traduzida de mais "
            "de um jeito nas páginas já traduzidas — mas isso vale só pro que já "
            "foi traduzido (e só pra correspondência exata; paráfrases da mesma "
            "ideia não são pegas)."
        )
        lines.append("")

    lines.append("| Ocorrências | Frase original (EN) | Tradução canônica (PT-BR) | Páginas |")
    lines.append("| --- | --- | --- | --- |")
    for k, locs in items:
        en_example = locs[0][1].replace("|", "\\|")
        pt = alignment.get(k, "").replace("|", "\\|")
        pages = sorted({code for code, _, _ in locs}, key=lambda c: (len(c), c))
        pages_str = ", ".join(pages)
        if k in divergences:
            pt_cell = "⚠️ " + pt
        elif pt:
            pt_cell = pt
        else:
            pt_cell = "_(a definir)_"
        lines.append(f"| {len(locs)}x | {en_example} | {pt_cell} | {pages_str} |")
    lines.append("")
    return "\n".join(lines)


def main():
    en = load_json(EN_JSON_PATH)
    pt = build_pt_dataset()

    en_blocks = index_dataset(en)
    pt_blocks = index_dataset(pt, id_remap=CATEGORY_ID_PT_TO_EN)

    repeated = build_repeated_sentence_index(en_blocks)
    variants = build_pt_variants(en_blocks, pt_blocks)
    divergences = find_divergences(variants)
    sys.stdout.write(render_markdown(repeated, variants, divergences))


if __name__ == "__main__":
    main()
