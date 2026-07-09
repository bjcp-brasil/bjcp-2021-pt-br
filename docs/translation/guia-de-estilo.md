# Guia de Estilo de Tradução

Convenções de tom e formatação decididas ao longo do projeto. Objetivo:
manter consistência entre os ~170 arquivos `.tex` sem exigir que cada
tradutor redescubra as mesmas regras.

## Princípios gerais

- **Fidelidade ao original antes de fluência.** Quando as duas entram em
  conflito, prefira uma tradução mais literal mas correta a uma reescrita
  livre que perca nuance técnica (ex.: intensidade de um defeito sensorial,
  faixa de valores).
- **Termos técnicos seguem o [glossário](glossario-en-pt.md).** Não
  traduza livremente `dry-hopping`, `funky`, `drinkability`, `crisp` — já
  foi decidido mantê-los em inglês.
- **Unidades e siglas (OG, FG, IBU, SRM, ABV) não são traduzidas.**

## Convenções de formatação

- Números de estatísticas (OG/FG/IBU/SRM/ABV) devem bater exatamente com
  bjcp.org/style/2021 — sempre confirme contra a versão 2021 do site
  (existem versões antigas do guia publicadas lá também).
- Nomes de estilo mantêm a grafia oficial do BJCP entre parênteses quando
  o nome em português seria ambíguo (ex. "IPA especial (Belgian IPA)").
- Notas do tradutor usam o padrão `\textit{(Nota do tradutor: ...)}` — ver
  exemplos em `glossario.tex`. Use com moderação, só quando a adaptação
  cultural não é óbvia a partir da tradução em si.

## Erros recorrentes de revisão (ortografia)

Padrões que apareceram repetidamente na auditoria de ortografia e vale
checar de novo em textos novos:

- Acentuação de palavras oxítonas/paroxítonas terminadas em `-vel`, `-cia`
  (ex.: "possível" vs "possivel").
- Crase antes de palavras femininas em expressões de intensidade ("à base
  de", "à percepção").
- Uso de hífen em compostos técnicos (ex.: "pós-fermentação").

## O que NÃO fazer

- Não reabra decisões já documentadas em
  [`decisoes-editoriais.md`](decisoes-editoriais.md) sem novo argumento —
  casos como "Session Strength" → "Teor alcoólico leve" e "Kellerbier"
  já foram investigados e confirmados corretos contra o próprio glossário
  do documento.
- Não use ferramentas de tradução automática/IA para *comparar* com o
  texto oficial sem verificar a citação exata — resumos/paráfrases (ex.:
  de web fetchers) podem perder a redação literal necessária pra avaliar
  fidelidade.
