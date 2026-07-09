# Registro de Decisões Editoriais

Casos investigados durante revisões de tradução onde a primeira impressão
era "isso parece um erro", mas a investigação confirmou que a tradução
está correta (ou foi corrigida por um motivo específico não óbvio). Consulte
antes de reabrir qualquer um destes pontos.

## Falsos positivos confirmados (auditoria de qualidade)

### 25B Saison — "Session Strength"

Parecia que "Session Strength" deveria virar algo mais literal. Na
verdade o documento já define, no seu próprio glossário de tags
(`referencias-de-tags-de-estilo.tex`, tag `session-strength`), a tradução
oficial como **"Teor-alcoólico-leve"**. A tradução no corpo do texto segue
essa convenção corretamente. Não é erro — não alterar sem mudar também a
tabela de tags (o que exigiria uma decisão nova e deliberada, não uma
correção pontual).

### 27A Kellerbier — "Specialty-Type Beers"

Mesma situação: "cervejas especiais" como tradução de "Specialty-Type
Beers" bate com a convenção de `specialty-beer` → "Família-das-cervejas-de
especialidade" já estabelecida no glossário de tags. Confirmado como
correto, não como erro de tradução.

## Termos deliberadamente não traduzidos

Ver [`glossario-en-pt.md`](glossario-en-pt.md#termos-mantidos-em-inglês-não-traduzir)
para a lista completa (`dry-hopping`, `funky`, `drinkability`, `crisp`) e o
porquê de cada um.

## Pendências identificadas mas não corrigidas

### Tags de Região de Origem: western/eastern invertidos

Ao consolidar o glossário (ver nota em `glossario-en-pt.md`), notou-se que
`western-europe` está mapeado para "Europa-Oriental" e `eastern-europe`
para "Europa-Ocidental" — os pares parecem trocados. Isso não foi
verificado contra o original em inglês nem corrigido, porque não foi
capturado pela auditoria de tradução original (é uma tabela estrutural,
não prosa comparada estilo a estilo). **Ação recomendada**: confirmar
contra bjcp.org/style/2021 antes de alterar — pode ser assim mesmo no
original, ou pode ser erro de tradução legado.

## Como adicionar uma entrada aqui

Sempre que investigar um "isso parece errado" e a conclusão for "na
verdade está certo" (ou "está errado mas não vamos mudar agora, e eis o
motivo"), registre aqui. O objetivo é nunca gastar tempo reinvestigando o
mesmo ponto duas vezes.
