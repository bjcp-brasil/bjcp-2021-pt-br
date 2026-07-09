# Glossário EN → PT-BR

Termos técnicos e convenções de tradução consolidados a partir do próprio
guia (`introducao-aos-estilos-de-cerveja/glossario.tex` e
`referencias-de-tags-de-estilo.tex`) e das decisões tomadas durante a
auditoria de qualidade de tradução. Use como referência antes de traduzir
um termo novo — se já foi decidido aqui, não reabra a discussão sem motivo.

## Termos mantidos em inglês (não traduzir)

Termos sem equivalente direto em português ou cujo uso em inglês já é
consolidado na comunidade cervejeira brasileira. Traduzir criaria
estranhamento maior que manter o original.

| Termo | Por quê mantido |
|---|---|
| `dry-hopping` | Termo técnico consolidado, sem tradução natural |
| `funky` / `funk` | Sem palavra equivalente em PT-BR; amplamente usado no meio cervejeiro artesanal brasileiro |
| `drinkability` | Traduções existentes ("tomabilidade", "bebabilidade") soam artificiais; consenso é manter original |
| `crisp` | Sem palavra única equivalente — ver nota de tradução no glossário (final seco, limpo, bem definido) |
| Unidades: `OG`, `FG`, `IBU`, `SRM`, `ABV` | Siglas técnicas internacionais, mantidas como no original |

## Tags de atributo de estilo (EN → PT-BR)

Convenção oficial do documento (`referencias-de-tags-de-estilo.tex`) — usada
para categorizar estilos por teor alcoólico, cor, fermentação, origem,
família e sabor dominante. **Sempre siga esta tabela**, não traduza esses
termos livremente em outros pontos do texto.

### Teor Alcoólico (Strength)

| EN | PT-BR |
|---|---|
| session-strength | Teor-alcoólico-leve |
| standard-strength | Teor-alcoólico-padrão |
| high-strength | Teor-alcoólico-alto |
| very-high-strength | Teor-alcoólico-muito-alto |

### Cor (Color)

| EN | PT-BR |
|---|---|
| pale-color | Cor-clara |
| amber-color | Cor-âmbar |
| dark-color | Cor-escura |

### Fermentação / Maturação

| EN | PT-BR |
|---|---|
| top-fermented | Alta-fermentação |
| bottom-fermented | Baixa-fermentação |
| any-fermentation | Qualquer-fermentação |
| wild-fermented | Fermentação-selvagem |
| lagered | Condicionada-a-frio |
| aged | Maturada |

### Região de Origem

| EN | PT-BR |
|---|---|
| british-isles | Ilhas-Britânicas |
| western-europe | Europa-Oriental* |
| central-europe | Europa-Central |
| eastern-europe | Europa-Ocidental* |
| north-america | América-do-Norte |
| south-america | América-do-Sul |
| pacific | Pacífico |

\* Sim, `western-europe` está mapeado para "Europa-Oriental" e
`eastern-europe` para "Europa-Ocidental" no documento original — isso é
uma inversão em relação ao esperado. Não corrigido ainda porque não foi
identificado durante a auditoria de tradução (essa tabela é estrutural,
não prosa). **Candidato a fix em revisão futura** — confirmar contra o
guia oficial antes de alterar.

### Família de Estilo

Nomes de família (`ipa-family`, `stout-family`, etc.) seguem o padrão
`Família-das-<nome>` ou `Família-<nome>` — ver tabela completa em
`referencias-de-tags-de-estilo.tex`.

### Sabor Dominante

| EN | PT-BR |
|---|---|
| malty | Maltado |
| bitter | Amargo |
| balanced | Equilibrado |
| hoppy | Lupulado |
| roasty | Tostado |
| sweet | Adocicado |
| smoke | Defumado |
| sour | Ácido/Azedo |
| wood | Amadeirado |
| fruit | Frutado |
| spice | Condimentado |

## Termos com nota de tradução (adaptação cultural)

| Termo original | Tradução/nota |
|---|---|
| Bubblegum (Bazooka) | Referência adaptada para "goma de mascar Bubbaloo tutti-frutti" — equivalente local reconhecível |

## Como usar este glossário

- Termo novo apareceu numa tradução? Procure aqui primeiro.
- Não está aqui e não é óbvio? Registre a decisão em
  [`decisoes-editoriais.md`](decisoes-editoriais.md) depois de resolvido,
  não só no commit.
- Tags de atributo (`referencias-de-tags-de-estilo.tex`) são estruturais —
  qualquer estilo novo (ex.: revisão 2026+ do BJCP) deve reusar essas
  traduções exatas, não reinventar.
