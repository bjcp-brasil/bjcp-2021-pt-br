# Rubrica de Qualidade de Tradução (0–10)

Critério usado na auditoria de qualidade que avaliou os 123 estilos do
guia (comparando cada `.tex` com o texto oficial em
bjcp.org/style/2021). Reuse esta rubrica em revisões futuras (nova versão
do BJCP, ou nova rodada de QA) para manter os resultados comparáveis.

## Dimensões avaliadas

1. **Fidelidade técnica** — a tradução preserva com exatidão valores,
   faixas, e afirmações condicionais do original (ex.: "pode estar
   presente" vs "deve estar presente")? Erros aqui pesam mais que
   qualquer outra dimensão.
2. **Terminologia consistente** — os termos seguem o
   [glossário](glossario-en-pt.md) e as tags oficiais? Termo traduzido de
   forma diferente em estilos diferentes é penalizado.
3. **Fluência em português** — a frase soa natural em PT-BR ou é uma
   tradução literal desajeitada (calco sintático do inglês)?
4. **Completude** — nada foi omitido ou adicionado em relação ao
   original.
5. **Ortografia/gramática** — erros de acentuação, concordância, crase.

## Escala

| Nota | Critério |
|---|---|
| 9–10 | Sem problemas relevantes em nenhuma dimensão |
| 7–8 | Pequenos desvios de fluência ou terminologia, sem afetar sentido |
| 5–6 | Um erro técnico ou de terminologia que pode confundir o leitor |
| 3–4 | Múltiplos erros, ou um erro técnico que muda o sentido |
| 0–2 | Tradução incompleta, sentido invertido, ou seção ausente |

## Processo recomendado

1. Buscar o texto oficial exato (não resumido) do estilo em
   bjcp.org/style/2021 — confirmar que é a versão 2021, não uma versão
   antiga arquivada no mesmo domínio.
2. Comparar parágrafo a parágrafo com o `.tex` traduzido.
3. Aplicar a rubrica acima, registrar nota + observações.
4. Antes de tratar uma discrepância como erro, checar se já não é uma
   decisão editorial documentada — ver
   [`decisoes-editoriais.md`](decisoes-editoriais.md) (casos de falso
   positivo já aconteceram: 25B Saison e 27A Kellerbier pareciam erro de
   tradução mas seguiam convenção própria do glossário do documento).
5. Registrar resultado consolidado (ex.: gist ou artefato compartilhável)
   pra dar visibilidade sem poluir o histórico de commits.
