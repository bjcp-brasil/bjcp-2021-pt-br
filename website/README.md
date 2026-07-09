# Versão web do guia (Docusaurus)

Gera a versão web publicada em GitHub Pages a partir dos mesmos `.tex` do
PDF, usando [Docusaurus](https://docusaurus.io/). Substituiu o pipeline
anterior baseado em `pandoc` + `sed` manual.

## Premissa

O `.tex` na raiz do repositório continua sendo **a única fonte da verdade**
(é dele que o PDF é gerado). Nada aqui edita ou substitui os `.tex`.
`website/docs/` é **gerado, não versionado** (está no `.gitignore`) —
recriado do zero a cada build, local ou no CI, por
[`scripts/generate-docs.mjs`](scripts/generate-docs.mjs).

## Como funciona

Diferente de um manifesto escrito à mão, a ordem e a estrutura são lidas
**automaticamente**:

1. `scripts/generate-docs.mjs` parseia os `\input{...}` de `../main.tex`,
   em ordem, pra descobrir as 34 categorias + apêndices.
2. Pra cada categoria (`\input{DIR/index.tex}`), lê `DIR/header.tex` pro
   label e `DIR/index.tex` pro `_category_.json` (label + posição) e pra
   descobrir, também automaticamente, a ordem real dos arquivos de estilo
   dentro dela (não é sempre alfabética — ex.: `21b-specialty-ipa.tex`
   vem antes de `21b-specialty-ipa-belgian-ipa.tex` no guia, mas seria o
   contrário em ordem alfabética de string).
3. Arquivos "soltos" referenciados direto em `main.tex` (não são uma
   categoria com header.tex/index.tex) viram página única — ou, se tiverem
   `\input` aninhado pra outros `.tex` (caso do Apêndice B, que inclui 5
   estilos regionais), viram uma pseudo-categoria: cada `\input` aninhado
   também ganha página própria, do mesmo jeito que qualquer estilo normal.
4. `frontpage.tex` (capa: título, logo, créditos, versão) é tratado à
   parte, vira `capa.md` na raiz do site (`/`).
5. `docusaurus build` consome `docs/` normalmente — sidebar é
   **autogerada** a partir da estrutura de pastas/arquivos.

Busca é local (`@easyops-cn/docusaurus-search-local`, indexada no build),
sem depender de conta/API externa.

`numberPrefixParser` está desligado (`docusaurus.config.js`) — por padrão
o Docusaurus tira o número do início da URL (`21-ipa` → `/ipa/`), mas aqui
o número é a numeração oficial de categoria do BJCP e vale a pena manter
na URL (`/21-ipa/`).

## Rodando localmente

Requer Docker (pro passo do pandoc) e Node 20+.

```bash
node scripts/generate-docs.mjs   # gera website/docs/ a partir dos .tex
npm install
npm run start                    # dev server com hot reload
# ou
npm run build && npm run serve   # build de produção + preview local
```

## CI

- `.github/workflows/deploy-pages.yml`: a cada push em `main`, gera os
  `.md`, builda e publica em GitHub Pages.
- `.github/workflows/build-check.yml`: mesma coisa em qualquer outra
  branch, só que sem publicar — só pra pegar build quebrado antes do
  merge.
