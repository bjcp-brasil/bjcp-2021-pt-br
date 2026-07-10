#!/usr/bin/env python3
"""Converte bjcp-2021-pt-br.json (gerado por build_dataset.py) para .xml e
.yaml, seguindo a mesma convenção dos arquivos bjcp-2021.xml/.yaml em inglês
de https://github.com/bjcp-brasil/styleguide-2021 (arrays viram tags XML
repetidas, sem wrapper).

Requer PyYAML (`pip install pyyaml`).
"""
import json
import os
import xml.sax.saxutils as saxutils

HERE = os.path.dirname(__file__)
IN_JSON = os.path.join(HERE, "bjcp-2021-pt-br.json")
OUT_XML = os.path.join(HERE, "bjcp-2021-pt-br.xml")
OUT_YAML = os.path.join(HERE, "bjcp-2021-pt-br.yaml")


def to_xml(tag, value, indent):
    pad = "  " * indent
    if value is None:
        return f"{pad}<{tag}/>\n"
    if isinstance(value, dict):
        inner = "".join(to_xml(k, v, indent + 1) for k, v in value.items())
        return f"{pad}<{tag}>\n{inner}{pad}</{tag}>\n"
    if isinstance(value, list):
        return "".join(to_xml(tag, item, indent) for item in value)
    text = saxutils.escape(str(value))
    return f"{pad}<{tag}>{text}</{tag}>\n"


def build_xml(data):
    body = "".join(to_xml(k, v, 1) for k, v in data["styleguide"].items())
    return (
        '<?xml version="1.0" encoding="UTF-8" ?>\n'
        f"<styleguide>\n{body}</styleguide>\n"
    )


def main():
    with open(IN_JSON, encoding="utf-8") as f:
        data = json.load(f)

    with open(OUT_XML, "w", encoding="utf-8") as f:
        f.write(build_xml(data))
    print(f"OK {OUT_XML}")

    import yaml

    class NoAliasDumper(yaml.SafeDumper):
        def ignore_aliases(self, _data):
            return True

    with open(OUT_YAML, "w", encoding="utf-8") as f:
        yaml.dump(
            data, f, Dumper=NoAliasDumper, allow_unicode=True,
            default_flow_style=False, sort_keys=False, width=1000,
        )
    print(f"OK {OUT_YAML}")


if __name__ == "__main__":
    main()
