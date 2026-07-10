# Gerador do dataset PT-BR (JSON/XML/YAML)

Gera a versão traduzida do [bjcp-brasil/styleguide-2021](https://github.com/bjcp-brasil/styleguide-2021) a partir dos `.tex` deste repositório.

```bash
python3 tools/styleguide-dataset/build_dataset.py     # gera bjcp-2021-pt-br.json
pip install pyyaml
python3 tools/styleguide-dataset/convert_formats.py    # gera .xml e .yaml a partir do .json
```

Requer Docker (usa `pandoc/core:2.9`, mesma imagem do pipeline do site).

Os 3 arquivos gerados (`bjcp-2021-pt-br.json/.xml/.yaml`, ignorados pelo git
neste repositório) devem ser copiados manualmente pra raiz de
`bjcp-brasil/styleguide-2021` e commitados lá — este script não escreve
direto no outro repositório.

Rode de novo sempre que o `.tex` mudar de forma que afete o conteúdo do
guia (novo estilo, correção de texto, etc.) e o dataset em
`styleguide-2021` estiver defasado.
