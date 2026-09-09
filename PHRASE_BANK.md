# Banco de frases repetidas

O guia original em inglês repete muitas frases padronizadas entre estilos (ex.: "The entrant must specify the type(s) of fruit used."). Esta lista existe pra garantir que, ainda que traduzidas por pessoas diferentes, essas frases fiquem com a mesma redação em PT-BR.

Gerado por [`scripts/generate-phrase-bank.py`](scripts/generate-phrase-bank.py) a partir do texto original em inglês vendorizado em [`scripts/bjcp-2021-en.json`](scripts/bjcp-2021-en.json) (dataset estruturado do Guia de Estilos 2021 do BJCP, via [bjcp-brasil/styleguide-2021](https://github.com/bjcp-brasil/styleguide-2021)) comparado com o texto PT-BR atual das páginas `.tex` deste repositório (regenerado a cada execução por [`tools/styleguide-dataset/build_dataset.py`](tools/styleguide-dataset/build_dataset.py)). Considera frases com 2+ ocorrências idênticas no original em inglês (comparação exata, após normalizar espaços/aspas/travessão) — variações de redação da mesma ideia não são detectadas automaticamente.

**210 frases repetidas** encontradas, cobrindo 621 ocorrências no total. **187/210** já têm uma tradução canônica sugerida — extraída de páginas já traduzidas ou, quando marcado "pré-definido", combinada antes de qualquer página ter traduzido a frase (ver [`scripts/phrase-bank-overrides.json`](scripts/phrase-bank-overrides.json)).

## Como usar

- Traduzindo ou revisando uma página: se uma frase dela aparece nesta lista **com** tradução canônica preenchida, use essa mesma redação.
- Se aparece na lista **sem** tradução canônica (coluna vazia), essa é a primeira vez que a frase está sendo traduzida — escolha a redação e, depois, rode o script de novo pra ela entrar como canônica pras próximas ocorrências.
- Depois de traduzir/revisar uma página, regenere este arquivo: `python3 scripts/generate-phrase-bank.py > PHRASE_BANK.md` (precisa de Docker rodando, usado pelo `build_dataset.py`).

## ⚠️ 59 divergência(s) encontrada(s)

A mesma frase em inglês foi traduzida de mais de um jeito em páginas diferentes. Escolha uma redação e corrija as demais páginas pra convergir.

- EN: Low malt aroma optional, but may be perceived as grainy, sweet, or corn-like, if present.
  - "Aroma de malte baixo é opcional, mas pode ser percebido como granulado, adocicado ou que remete a cereais, se presente." — 1A
  - "Aroma de malte baixo é opcional, mas pode ser percebido como cereais, adocicado ou semelhante a milho, se presente." — 1B
- EN: Clean fermentation profile.
  - "Perfil limpo de fermentação." — 1A, 7A, 7B, 18A, 18B
  - "Perfil de fermentação limpo." — 2A, 2B, 4A, 4B, 4C, 5A, 5C, 5D, 6A, 6B, 8A, 9C
  - "Caráter de fermentação limpo." — 8A
- EN: Strong flavors are a fault.
  - "Sabores fortes significam falha na cerveja." — 1A
  - "Sabores fortes são considerados um defeito." — 1B
- EN: Medium-light to medium body.
  - "Corpo de médio-baixo a médio." — 1D, X1, 26A
  - "Corpo de médio-leve a médio." — 3A, 8B, 11B, 13B, 13C, 18A, 18B
- EN: Moderate to low carbonation.
  - "Carbonatação de baixa a moderada." — 3B, 3C
  - "Carbonatação de moderada a baixa." — 3D
- EN: Low diacetyl optional.
  - "Diacetil baixo é opcional." — 3C, 13A, 13C, 17B
  - "Baixo diacetil é opcional." — 3C
  - "Um baixo nível de diacetil é opcional." — 12A
  - "Diacetil baixo opcional." — 16A, 16C, 16D
- EN: Clear to bright clarity.
  - "Clareza de limpa a brilhante." — 3C
  - "De límpida a brilhante." — 3D
- EN: Large, off-white, persistent head.
  - "Colarinho de alta formação, quase branco e persistente." — 3C
  - "Colarinho espesso, quase branco e persistente." — 7A
- EN: Low to moderate spicy hop flavor.
  - "Sabor condimentado de lúpulo de baixo a moderado." — 3C
  - "Sabor de lúpulo condimentado de baixo a moderado." — 3D
- EN: Continental Pilsner malt.
  - "Malte Pilsner da Europa continental." — 4A
  - "Malte Pilsner Europeu continental." — 5D
- EN: Moderate to moderately-high carbonation.
  - "Carbonatação de moderada a moderadamente alta." — 4C, 8B, 19C
  - "Carbonatação moderada a moderadamente alta." — 16C, 16D
- EN: Medium to medium-high carbonation.
  - "Carbonatação de média a média-alta." — 5B, 7B, X5, 13B, 19B, 21A, 22A
  - "Carbonatação de média a médio-alta." — 6B
  - "Carbonatação média a média-alta." — 16B, 24B
- EN: Malt and hop flavors similar to aroma (same descriptors and intensities).
  - "Sabores de malte e lúpulo similar ao aroma (com os mesmos descritores e intensidades)." — 5C
  - "Sabor de malte e lúpulo similar ao aroma (mesmos descritores e intensidades)." — 5D
- EN: Medium to medium-full body.
  - "Corpo de médio a médio-cheio." — 5C, 19A, 19C, 21C, 23C
  - "Corpo de médio a médio-alto." — 20A
- EN: Low spicy, herbal, or floral hop flavor optional.
  - "Sabor de lúpulo condimentado, herbal e/ou floral de baixa intensidade é opcional." — 8A
  - "Sabor de lúpulo condimentado, herbal e/ou floral baixo é opcional." — 10B
- EN: Medium-full to full body.
  - "Corpo de médio-cheio a cheio." — 9A, 22D
  - "Corpo de médio-alto a alto." — 10C
- EN: Light vanilla optional.
  - "Leve toque de baunilha é opcional." — 10A
  - "Leve baunilha é opcional." — 10A
- EN: Bubblegum, sourness, or smoke are faults.
  - "Bubblegum/Tuttifrutti, acidez e defumado são falhas." — 10A
  - "Bubblegum/Tuttifrutti (morango com banana), acidez e defumado são falhas." — 10B
- EN: Malted wheat, at least half the grist.
  - "Malte de trigo, pelo menos metade do perfil de maltes." — 10A, 10B
  - "Pelo menos metade da lista de grãos de malte de trigo." — 10C
- EN: Weizen yeast, cool fermentation temperatures.
  - "Levedura weizen, temperatura baixa de fermentação." — 10A
  - "Levedura weizen e temperaturas mais baixas de fermentação." — 10B
  - "Levedura Weizen e fermentação a temperatura fria." — 10C
- EN: Medium-light to medium-full body.
  - "Corpo de médio-leve a médio-cheio." — 10B, 11C
  - "Corpo de médio-baixo a médio-alto." — 23G
- EN: Moderate to high carbonation.
  - "Carbonatação de moderada a alta." — 10C, 18B
  - "Carbonatação moderada a alta." — 24C
- EN: Drinkability is a critical component of the style.
  - "A facilidade de consumo é um componente crítico do estilo." — 11A, 11B
  - "A facilidade em beber é um componente crítico do estilo." — 11C
- EN: English finishing hops are most traditional, but any hops are fair game; if American hops are used, a light touch is required.
  - "Lúpulos de finalização ingleses são os mais tradicionais, mas qualquer lúpulo é permitido; se forem usados lúpulos americanos, é necessário um toque suave." — 11A
  - "Lúpulos de finalização ingleses são os mais tradicionais, mas qualquer lúpulo é aceitável; se forem usados lúpulos americanos, é necessário um leve toque." — 11C
- EN: Medium-dry to dry finish.
  - "Final de meio-seco a seco." — 11C
  - "Final de meio seco a seco." — 12A
  - "Final meio seco a seco." — 15A
- EN: Some clean alcohol flavor can be noted in stronger versions.
  - "Algum sabor de álcool limpo pode ser notado em versões com maior teor alcoólico." — 12C
  - "Algum sabor limpo de álcool pode ser notado em versões mais fortes." — X2
- EN: Low earthy or floral hop aroma optional.
  - "Aroma baixo de lúpulo terroso ou floral é opcional." — 13A, 15B
  - "Aroma baixo de lúpulo terroso ou floral opcional." — 15A
- EN: Low hop flavor optional.
  - "Sabor de lúpulo baixo é opcional." — 13A
  - "Baixo sabor de lúpulo opcional." — 16C
- EN: Medium to medium-low bitterness.
  - "Amargor de médio a médio-baixo." — 13B
  - "Amargor médio a médio-baixo." — 15A
- EN: A slight roast dryness offsets the residual sweetness in the finish, with the bitterness perceived only to keep the beer from being cloying.
  - "Uma leve secura proveniente de torra compensa o dulçor residual no final, com o amargor percebido apenas para evitar que a cerveja seja enjoativa." — 14A
  - "Uma leve secura proveniente de torra compensa a doçura residual no final, com o amargor percebido apenas para evitar que a cerveja seja enjoativa." — 14B, 14C
- EN: Sufficient bitterness to not be cloying, but with a malty balance and aftertaste.
  - "Amargor suficiente para não ser enjoativa, mas com equilíbrio e retrogosto de maltado." — 14A, 14B
  - "Amargor suficiente para não ser enjoativa, mas com equilíbrio e retrogosto maltados." — 14C
- EN: Low to moderate carbonation.
  - "Carbonatação de baixa a moderada." — 14A, 14B, 17A, 20C, 22D
  - "Carbonatação baixa a moderada." — 15B, 16A, 23C
- EN: Pale copper to brown.
  - "De cobre claro a marrom." — 14B
  - "Cor de cobre claro a marrom." — 14C
- EN: Medium-low to medium carbonation.
  - "Carbonatação de médio-baixa a média." — 14C
  - "Carbonatação de média-baixa a média." — 22B
- EN: Low esters optional.
  - "Ésteres baixos opcionais." — 15A, 21A
  - "Ésteres baixos são opcionais." — 20B
- EN: The level of bitterness is somewhat variable, as is the roasted character and the dryness of the finish; allow for interpretation by brewers.
  - "O nível de amargor é um pouco variável, assim como o caráter torrado e a secura do final; permitindo interpretação pelos cervejeiros." — 15B
  - "O nível de amargor é um pouco variável, assim como o caráter torrado e a secura do final; permitindo a interpretação pelos cervejeiros." — 15C
- EN: Clear, if not opaque.
  - "Límpida, se não for opaca." — 16A, 16C, 16D
  - "Límpida, se não opaca." — 20A
  - "Límpida, quando não opaca." — 30B
- EN: Stronger versions may be lightly warming.
  - "Versões com teor alcoólico mais alto podem aquecer levemente." — 16B
  - "Versões mais fortes podem ter leve aquecimento alcoólico." — 19C
- EN: Large tan to brown head with good retention.
  - "Colarinho volumoso castanho a marrom, com boa retenção." — 16C
  - "Colarinho volumoso, castanho a marrom, com boa retenção." — 16D
- EN: Medium to high bitterness.
  - "Amargor médio a alto." — 16D
  - "Amargor de médio a alto." — 20B
- EN: High alcohol and viscosity may be visible as legs.
  - "O alto teor alcoólico e a viscosidade podem ser visíveis como lágrimas." — 17D
  - "O alto teor alcoólico e viscosidade podem ser visíveis como lágrimas." — 20C
  - "O alto teor alcoólico e a viscosidade podem ser visíveis como lágrimas (pernas)." — 22D
- EN: Full-bodied and chewy, with a velvety, luscious texture, declining with age.
  - "Encorpada e densa (com dextrinas), com uma textura aveludada e deliciosa, diminuindo com a idade." — 17D
  - "Encorpada e altamente viscosa, com uma textura aveludada e envolvente, diminuindo com a idade." — 22C
- EN: Carbonation may be low to moderate, depending on age and conditioning.
  - "A carbonatação pode ser de baixa a moderada, dependendo da idade e do acondicionamento." — 17D
  - "A carbonatação pode ser baixa a moderada, dependendo da idade e do acondicionamento." — 22C
- EN: Stronger versions may have a slight alcohol warmth.
  - "Versões com teor alcoólico mais alto podem ter um leve aquecimento alcoólico." — 19A
  - "Versões mais fortes podem ter um leve aquecimento alcoólico." — 20A
- EN: Should not seem sharp, acrid, or acidic.
  - "Não deve parecer pungente, acre ou ácida." — 20A
  - "Não deve parecer agressiva, acre ou ácida." — 20B
- EN: Medium to full body.
  - "Corpo de médio a alto." — 20B
  - "Corpo de médio a cheio." — 22B
- EN: Medium-light to medium body, with a smooth texture.
  - "Corpo de médio-leve a médio, com uma textura suave." — 21A
  - "Corpo de médio-leve a médio, com uma textura macia." — 22A
- EN: Clarity ranges from clear to somewhat hazy.
  - "A limpidez varia de transparente a um tanto turva." — 23A
  - "Limpidez varia de muito límpida até um pouco turva." — 28D
- EN: Large, dense, white head with poor retention.
  - "Colarinho branco alto, denso e com retenção pobre." — 23A
  - "Colarinho branco, denso e alto, com baixa retenção." — 28D
- EN: Fruited versions should be entered as a 29A Fruit Beer.
  - "Versões com adição de fruta devem ser inscritas como uma 29A Fruit Beer." — 23B
  - "Versões com frutas devem ser inscritas como uma 29A Fruit Beer." — 23C
- EN: Light to medium-light body; should not be watery.
  - "Corpo de baixo a médio-baixo; não deve ser aguada." — 23D
  - "Corpo baixo a médio-baixo; não deve ser aguada." — 23F
- EN: A noticeable vinegary or cidery character is considered a fault by Belgian brewers.
  - "Um caráter avinagrado ou de cidra perceptível é considerado um defeito pelos cervejeiros belgas." — 23D
  - "Um caráter perceptível avinagrado ou de cidra é considerado um defeito pelos cervejeiros belgas." — 23E
- EN: Medium to medium-light body.
  - "Corpo médio a médio-leve." — 24B
  - "Corpo de médio-baixo a médio." — X5
- EN: Most commercial examples are in the 6.5 – 7% ABV range.
  - "A maioria dos exemplos comerciais estão na faixa de 6,5 a 7% de ABV." — 25A
  - "A maioria dos exemplos comerciais estão na faixa de 6,5 a 7,0% de ABV." — 26B
- EN: Clarity can be variable; some haze is not a fault.
  - "Limpidez pode variar; turbidez baixa não é necessariamente uma falha." — 28B
  - "Limpidez variável; leve turbidez não é uma falha." — 28C
- EN: Can also be a blend of styles.
  - "Pode também ser uma mistura de estilos." — 28B
  - "Pode ser ainda uma mistura de estilos." — 28C
- EN: The Specialty-Type Ingredients should be evident, as well as the defining characteristics of a wild fermentation per the base style.
  - "O ingrediente especial deve ser evidente, assim como as características de uma fermentação selvagem esperadas para o estilo base." — 28C
  - "O ingrediente especial deve ser evidente assim como as características de uma fermentação selvagem esperadas para o estilo base." — 28C
- EN: SHVs may increase or decrease body.
  - "Algumas SHVs podem aumentar ou diminuir o corpo." — 29B
  - "SHVs podem aumentar ou diminuir o corpo." — 30A
- EN: Some SHVs may add a bit of astringency, although a "raw" spice character is undesirable.
  - "Alguns SHVs podem adicionar um pouco de adstringência, ainda que um caráter de especiaria "crua" não seja desejável." — 29B
  - "Alguns SHVs podem adicionar um pouco de adstringência, ainda que um caráter de especiaria "crua" seja indesejável." — 30A

| Ocorrências | Frase original (EN) | Tradução canônica (PT-BR) | Páginas |
| --- | --- | --- | --- |
| 27x | Clean fermentation profile. | ⚠️ Perfil de fermentação limpo. | 1A, 1B, 2A, 2B, 2C, 4A, 4B, 4C, 5A, 5C, 5D, 6A, 6B, 7A, 7B, 8A, 9A, 9B, 9C, 18A, 18B |
| 13x | A general description of the special nature of the beer can cover all the required items. | _(a definir)_ | 28C, 29A, 29B, 29C, 30A, 30B, 30C, 30D, 31A, 31B, 32B, 33A, 33B |
| 11x | Low diacetyl optional. | ⚠️ Diacetil baixo é opcional. | 3C, 12A, 13A, 13C, 16A, 16C, 16D, 17B |
| 11x | Variable by base style. | Varia com o estilo base. | 28A, 28B, 28C |
| 11x | Entrant must specify a description of the beer, identifying either a Base Style or the ingredients, specs, or target character of the beer. | _(a definir)_ | 29A, 29C, 30A, 30B, 30C, 30D, 31A, 31B, 32B, 33A, 33B |
| 10x | Medium-light to medium body. | ⚠️ Corpo de médio-leve a médio. | 1D, 3A, 8B, X1, 11B, 13B, 13C, 18A, 18B, 26A |
| 10x | Medium to medium-high carbonation. | ⚠️ Carbonatação de média a média-alta. | 5B, 6B, 7B, X5, 13B, 16B, 19B, 21A, 22A, 24B |
| 10x | Varies with base style. | Varia de acordo com o estilo base. | 33A, 33B |
| 9x | Varies by base style. | Varia de acordo com o estilo base. | 29A, 29B, 30A |
| 8x | Medium to high carbonation. | Carbonatação de média a alta. | 2B, 2C, 5A, 5D, X1, X4, 18A, 19A |
| 8x | Low to moderate carbonation. | ⚠️ Carbonatação de baixa a moderada. | 14A, 14B, 15B, 16A, 17A, 20C, 22D, 23C |
| 7x | Clear, if not opaque. | ⚠️ Límpida, se não for opaca. | 16A, 16B, 16C, 16D, 20A, 30B, 30C |
| 6x | Moderate carbonation. | Carbonatação moderada. | 3A, 7A, 8A, 15A, 15C, 17C |
| 6x | Traditional German hops. | Lúpulos tradicionais alemães. | 4A, 4C, 5A, 5B, 5D, 9A |
| 6x | Medium to medium-full body. | ⚠️ Corpo de médio a médio-cheio. | 5C, 19A, 19C, 20A, 21C, 23C |
| 6x | Generally no diacetyl, although very low levels are allowed. | Geralmente sem diacetil, embora níveis muito baixos sejam permitidos. | 11A, 11B, 11C |
| 6x | See category introduction. | Veja a introdução da categoria. | 14A, 14B, 14C |
| 5x | Clean German lager yeast. | Levedura lager alemã limpa. | 4A, 5D, 6C, 7A, 9A |
| 5x | Moderate to moderately-high carbonation. | ⚠️ Carbonatação de moderada a moderadamente alta. | 4C, 8B, 16C, 16D, 19C |
| 5x | Decoction mash traditional. | Mostura por decocção é tradicional. | 5C, 8A, 10A, 10B, 10C |
| 5x | The description of the beer is critical for evaluation; judges should think more about the declared concept than trying to detect each individual ingredient. | _(a definir)_ | 29A, 29B, 30A, 30B, 30C |
| 5x | Balance, drinkability, and execution of the theme are the most important deciding factors. | _(a definir)_ | 29A, 29B, 30A, 30B, 30C |
| 5x | Based on declared beer. | De acordo com a cerveja declarada. | 34A |
| 4x | Light to medium body. | Corpo de leve a médio. | 2A, 2B, 12A, 13A |
| 4x | Traditional Czech hops. | _(a definir)_ | 3A, 3B, 3C, 3D |
| 4x | Moderate to high carbonation. | ⚠️ Carbonatação de moderada a alta. | 10C, 18B, 24C, 28D |
| 4x | Good to brilliant clarity. | Limpidez de boa a brilhante. | 11A, 11B, 11C, 12A |
| 4x | No peat-smoked malt. | Sem malte defumado com turfa. | 14A, 14B, 14C, 17C |
| 4x | Should not have enteric, smoky, cigar-like, or cheesy faults. | Não deve apresentar defeitos entéricos, defumados, semelhantes a charutos ou de queijo. | 23D, 23E |
| 4x | Based on the declared Base Styles. | De acordo com os estilos base declarados. | 34B |
| 3x | Moderate to low carbonation. | ⚠️ Carbonatação de baixa a moderada. | 3B, 3C, 3D |
| 3x | Medium-full to full body. | ⚠️ Corpo de médio-cheio a cheio. | 9A, 10C, 22D |
| 3x | Bubblegum (strawberry with banana), sourness, or smoke are faults. | Bubblegum/Tuttifrutti (morango com banana), acidez e defumado são falhas. | 10A, 10B, 10C |
| 3x | Bubblegum, sourness, or smoke are faults. | ⚠️ Bubblegum/Tuttifrutti, acidez e defumado são falhas. | 10A, 10B, 10C |
| 3x | Malted wheat, at least half the grist. | ⚠️ Malte de trigo, pelo menos metade do perfil de maltes. | 10A, 10B, 10C |
| 3x | Weizen yeast, cool fermentation temperatures. | ⚠️ Levedura weizen, temperatura baixa de fermentação. | 10A, 10B, 10C |
| 3x | Medium-light to medium-full body. | ⚠️ Corpo de médio-leve a médio-cheio. | 10B, 11C, 23G |
| 3x | Drinkability is a critical component of the style. | ⚠️ A facilidade de consumo é um componente crítico do estilo. | 11A, 11B, 11C |
| 3x | Low to moderate white to off-white head. | Colarinho de branco a quase branco de baixo a moderado. | 11A, 11B, 11C |
| 3x | See comments in category introduction. | Veja os comentários na introdução da categoria. | 11A, 11B, 11C |
| 3x | English finishing hops are most traditional, but any hops are fair game; if American hops are used, a light touch is required. | ⚠️ Lúpulos de finalização ingleses são os mais tradicionais, mas qualquer lúpulo é permitido; se forem usados lúpulos americanos, é necessário um toque suave. | 11A, 11B, 11C |
| 3x | Characterful British yeast. | Levedura britânica com caráter presente. | 11A, 11B, 11C |
| 3x | Medium-dry to dry finish. | ⚠️ Final de meio-seco a seco. | 11C, 12A, 15A |
| 3x | Low earthy or floral hop aroma optional. | ⚠️ Aroma baixo de lúpulo terroso ou floral é opcional. | 13A, 15A, 15B |
| 3x | Moderate fruity esters optional. | Ésteres frutados moderados são opcionais. | 13A, 20A |
| 3x | A slight roast dryness offsets the residual sweetness in the finish, with the bitterness perceived only to keep the beer from being cloying. | ⚠️ Uma leve secura proveniente de torra compensa a doçura residual no final, com o amargor percebido apenas para evitar que a cerveja seja enjoativa. | 14A, 14B, 14C |
| 3x | Light pome fruitiness and light English hop aroma (earthy, floral, orange-citrus, spicy, etc.) allowable. | Leve frutado de maçã/pera e leve aroma de lúpulo inglês (terroso, floral, laranja-cítrico, picante, etc.) são permitidos. | 14A, 14B, 14C |
| 3x | Low to moderate, creamy off-white. | Colarinho cremoso, quase branco, de baixo a moderado. | 14A, 14B, 14C |
| 3x | Medium toasty-bready malt with caramel and toffee overtones, finishing with a slightly roasty dryness. | Malte médio como pão tostado, com nuances de caramelo e toffee, terminando com uma leve secura proveniente de torra. | 14A, 14B, 14C |
| 3x | A wide range of caramelized sugar and toasted bread type of flavors are possible, using similar descriptors as the aroma. | Uma ampla gama de sabores de açúcar caramelizado e pão tostado é possível, usando descritores semelhantes ao aroma. | 14A, 14B, 14C |
| 3x | Clean maltiness and fermentation profile. | Maltado e perfil de fermentação limpos. | 14A, 14B, 14C |
| 3x | Light esters and hop flavor allowable (similar descriptors as aroma). | Ésteres e sabor de lúpulo leves são permitidos (descritores semelhantes ao aroma). | 14A, 14B, 14C |
| 3x | Sufficient bitterness to not be cloying, but with a malty balance and aftertaste. | ⚠️ Amargor suficiente para não ser enjoativa, mas com equilíbrio e retrogosto de maltado. | 14A, 14B, 14C |
| 3x | Maybe be moderately creamy. | Pode ser moderadamente cremosa. | 14A, 14B, 14C |
| 3x | See category introduction for detailed comments. | Veja a introdução da categoria para comentários detalhados. | 14A, 14B, 14C |
| 3x | May not seem as bitter as specifications indicate due to higher finishing gravity and residual sweetness. | Pode não parecer tão amarga quanto as especificações indicam devido à densidade final maior e dulçor residual. | 14A, 14B, 14C |
| 3x | Do not mis-perceive the light roasty dryness as smoke; smoke is not present in these beers. | Não confunda a leve secura proveniente de torra com defumado; o defumado não está presente nessas cervejas. | 14A, 14B, 14C |
| 3x | The Shilling ale names were used for mild (unaged) beer before World War I, but the styles took modern form only after World War II. | Os nomes de cervejas Shilling eram usados para cervejas suaves (não envelhecidas) antes da Primeira Guerra Mundial, mas os estilos assumiram uma forma moderna apenas após a Segunda Guerra Mundial. | 14A, 14B, 14C |
| 3x | Low esters optional. | ⚠️ Ésteres baixos opcionais. | 15A, 20B, 21A |
| 3x | High alcohol and viscosity may be visible as legs. | ⚠️ O alto teor alcoólico e a viscosidade podem ser visíveis como lágrimas. | 17D, 20C, 22D |
| 3x | American or New World hops. | Lúpulo americano ou do novo mundo. | 18B, 22A, 22B |
| 3x | Moderately low to moderately high carbonation. | Carbonatação de moderadamente baixa a moderadamente alta. | 20A, 30B, 30C |
| 3x | Low to moderate esters. | Ésteres de baixos a moderados. | 22B, 22C, 24C |
| 3x | Light to medium-light body; should not be watery. | ⚠️ Corpo de baixo a médio-baixo; não deve ser aguada. | 23D, 23E, 23F |
| 3x | Varies by base style and special ingredients. | Varia de acordo com o estilo base e ingredientes especiais utilizados. | 29A, 29B, 30A |
| 3x | Variable clarity, although haze is generally undesirable. | Limpidez variável, ainda que a turbidez seja geralmente não desejável. | 29A, 29B, 30A |
| 3x | Some ingredients may impact head retention. | Alguns ingredientes podem impactar na retenção da espuma. | 29A, 29B, 30A |
| 3x | Added sugars should not have a raw, unfermented flavor. | Açúcares adicionados não devem ter um sabor cru, não fermentado. | 29C, 30D, 31B |
| 2x | Low malt aroma optional, but may be perceived as grainy, sweet, or corn-like, if present. | ⚠️ Aroma de malte baixo é opcional, mas pode ser percebido como granulado, adocicado ou que remete a cereais, se presente. | 1A, 1B |
| 2x | While a clean fermentation profile is desirable, a light amount of yeast character is not a fault. | Embora seja desejável um perfil de fermentação limpo, uma leve presença de caráter de levedura não é considerada um defeito. | 1A, 1B |
| 2x | White, frothy head seldom persists. | Colarinho branco, não muito persistente. | 1A, 1B |
| 2x | Balance may vary from slightly malty to slightly bitter, but is usually close to even. | Equilíbrio pode variar de ligeiramente maltado a ligeiramente amargo, mas geralmente é equilibrado. | 1A, 1B |
| 2x | High carbonation may accentuate the crispness of the dry finish. | A alta carbonatação pode realçar a nitidez do final seco. | 1A, 1B |
| 2x | Very highly carbonated with slight carbonic bite on the tongue. | Carbonatação muito alta, gera sensação de carbonatação picante na língua. | 1A, 1B |
| 2x | Strong flavors are a fault. | ⚠️ Sabores fortes significam falha na cerveja. | 1A, 1B |
| 2x | Two- or six-row barley with up to 40% rice or corn as adjuncts. | _(a definir)_ | 1A, 1B |
| 2x | Low to medium-low body. | Corpo de baixo a médio-baixo. | 1B, X4 |
| 2x | Low fruity esters optional. | Opcionalmente pode apresentar ésteres frutados de baixa intensidade. | 1C, 4C |
| 2x | Medium-high to high carbonation. | Carbonatação de média-alta a alta. | 1D, 20B |
| 2x | Light to medium-light body. | Corpo de leve a médio-leve. | 2C, 11A |
| 2x | Light yellow to deep gold color. | Cor de amarelo claro a dourado profundo. | 3A, X1 |
| 2x | Bitterness is prominent but never harsh. | Amargor é proeminente mas nunca áspero. | 3A, 3B |
| 2x | Clear to bright clarity. | ⚠️ Clareza de limpa a brilhante. | 3C, 3D |
| 2x | Large, off-white, persistent head. | ⚠️ Colarinho de alta formação, quase branco e persistente. | 3C, 7A |
| 2x | Low to moderate spicy hop flavor. | ⚠️ Sabor condimentado de lúpulo de baixo a moderado. | 3C, 3D |
| 2x | Low mineral content water. | _(a definir)_ | 3C, 3D |
| 2x | Continental Pilsner malt. | ⚠️ Malte Pilsner da Europa continental. | 4A, 5D |
| 2x | Medium-low to medium bitterness. | Amargor de médio-baixo a médio. | 5B, 8B |
| 2x | Malt and hop flavors similar to aroma (same descriptors and intensities). | ⚠️ Sabores de malte e lúpulo similar ao aroma (com os mesmos descritores e intensidades). | 5C, 5D |
| 2x | Traditional German or Czech hops. | _(a definir)_ | 5C, 6B |
| 2x | Clean lager fermentation character. | Perfil de fermentação lager limpo. | 6A, 6B |
| 2x | Smooth lager character. | Caráter lager suave. | 6B, 8A |
| 2x | Virtually no hop aroma. | Praticamente sem aroma de lúpulo. | 6C, 9A |
| 2x | Clean lager character. | Caráter lager limpo. | 7A, 8B |
| 2x | Low spicy, herbal, or floral hop flavor optional. | ⚠️ Sabor de lúpulo condimentado, herbal e/ou floral de baixa intensidade é opcional. | 8A, 10B |
| 2x | Light vanilla optional. | ⚠️ Leve toque de baunilha é opcional. | 10A |
| 2x | Light floral, spicy, or herbal hops optional. | Lúpulo floral, condimentado e/ou herbal de intensidade leve é opcional. | 10A, 10B |
| 2x | Munich, Vienna, or Pilsner malt. | Malte Munich, Vienna e/ou Pilsner. | 10B, 10C |
| 2x | Mild to moderate fruitiness. | Frutado de leve a moderado. | 11A, 11B |
| 2x | Hop aroma can range from moderate to none, typically with a floral, earthy, resiny, or fruity character. | O aroma de lúpulo pode variar de moderado a nenhum, tipicamente com um caráter floral, terroso, resinoso ou frutado. | 11A, 11B |
| 2x | May have very little head due to low carbonation. | Pode ter muito pouco colarinho devido à baixa carbonatação. | 11A, 11B |
| 2x | Medium to moderately high bitterness. | Amargor de médio a moderadamente alto. | 11A, 11B |
| 2x | Moderately low to moderately high fruity esters. | Ésteres frutados de moderadamente baixos a moderadamente altos. | 11A, 11B |
| 2x | Moderate to low hop flavor, typically with an earthy, resiny, fruity, or floral character. | Sabor de lúpulo de baixo a moderado, tipicamente com caráter terroso, resinoso, frutado e/ou floral. | 11A, 11B |
| 2x | Low to medium maltiness with a dry finish. | Maltado de baixo a médio com final seco. | 11A, 11B |
| 2x | The malt profile is typically bready, biscuity, or lightly toasty. | O perfil de malte é tipicamente de pão, biscoito ou levemente tostado. | 11A, 11B |
| 2x | Low to moderate caramel or toffee flavors are optional. | Sabores de caramelo ou toffee de baixo a moderado são opcionais. | 11A, 11B |
| 2x | Low carbonation, although bottled examples can have moderate carbonation. | Carbonatação baixa, embora exemplos engarrafados possam ter carbonatação moderada. | 11A, 11B |
| 2x | Pale ale, amber, or crystal malts. | Maltes pale ale, amber e/ou crystal. | 11A, 11B |
| 2x | May use sugar adjuncts, corn, or wheat. | Pode usar adjuntos como açúcar, milho ou trigo. | 11A, 12A |
| 2x | Emphasis is on the bittering hop addition as opposed to the aggressive middle and late hopping seen in American ales. | A ênfase está na adição de lúpulo de amargor, em oposição à agressiva adição de lúpulo intermediária e tardia vista em ales americanas. | 11A, 11B |
| 2x | A low head is acceptable when carbonation is also low. | Um colarinho baixo é aceitável quando a carbonatação também é baixa. | 11C, 12A |
| 2x | Some clean alcohol flavor can be noted in stronger versions. | ⚠️ Algum sabor de álcool limpo pode ser notado em versões com maior teor alcoólico. | X2, 12C |
| 2x | Very low diacetyl optional. | Diacetil muito baixo é opcional. | 13A, 22D |
| 2x | Low hop flavor optional. | ⚠️ Sabor de lúpulo baixo é opcional. | 13A, 16C |
| 2x | Low to moderate off-white to light tan head. | Colarinho de baixo a moderado, com cor de quase branco a castanho claro. | 13B, 19C |
| 2x | Medium to medium-low bitterness. | ⚠️ Amargor de médio a médio-baixo. | 13B, 15A |
| 2x | Low floral or earthy hop flavor optional. | Baixo sabor de lúpulo floral ou terroso é opcional. | 13B, 16A |
| 2x | Low to moderate fruity esters. | Ésteres frutados de baixo a moderado. | 13C, 16A |
| 2x | Medium-low to medium body. | Corpo médio-leve a médio. | 14A, 14B |
| 2x | Pale copper to brown. | ⚠️ De cobre claro a marrom. | 14B, 14C |
| 2x | At its simplest, pale ale malt and colored malt, but can also use sugars, corn, wheat, crystal malts, colorants, and a variety of other grains. | Na sua forma mais simples, malte pale ale e malte com mais cor, mas também pode usar açúcares, milho, trigo, malte crystal, corantes e uma variedade de outros grãos. | 14B, 14C |
| 2x | Medium-low to medium carbonation. | ⚠️ Carbonatação de médio-baixa a média. | 14C, 22B |
| 2x | Medium-low esters optional. | Ésteres médio-baixos opcionais. | 15B, 15C |
| 2x | The level of bitterness is somewhat variable, as is the roasted character and the dryness of the finish; allow for interpretation by brewers. | ⚠️ O nível de amargor é um pouco variável, assim como o caráter torrado e a secura do final; permitindo interpretação pelos cervejeiros. | 15B, 15C |
| 2x | May have a light astringency from the roasted grains, although harshness is undesirable. | Pode ter uma leve adstringência dos cereais torrados, embora a aspereza seja indesejável. | 15B, 15C |
| 2x | Medium-low diacetyl optional but typically absent. | Diacetil médio-baixo opcional, mas normalmente ausente. | 16B |
| 2x | Stronger versions may be lightly warming. | ⚠️ Versões com teor alcoólico mais alto podem aquecer levemente. | 16B, 19C |
| 2x | Stronger versions can have a subtle, clean aroma of alcohol. | Versões com teor alcoólico mais alto podem ter um aroma sutil e limpo de álcool. | 16C, 16D |
| 2x | Very deep brown to black in color. | Cor marrom muito profundo a preto. | 16C, 16D |
| 2x | Clarity usually obscured by deep color. | Limpidez geralmente obscurecida pela cor escura. | 16C, 16D |
| 2x | Large tan to brown head with good retention. | ⚠️ Colarinho volumoso castanho a marrom, com boa retenção. | 16C, 16D |
| 2x | Medium-low diacetyl optional. | Diacetil médio-baixo opcional. | 16C, 16D |
| 2x | May have a warming but not hot alcohol presence. | Pode ter um aquecimento alcoólico, mas não pode queimar. | 16C, 16D |
| 2x | May use adjuncts and sugar to boost gravity. | Pode usar adjuntos e açúcar para aumentar a densidade. | 16C, 16D |
| 2x | Medium to high bitterness. | ⚠️ Amargor médio a alto. | 16D, 20B |
| 2x | Alcohol warmth is often evident and always welcome. | O aquecimento alcoólico é muitas vezes evidente e sempre bem-vindo. | 17A, 17B |
| 2x | Full-bodied and chewy, with a velvety, luscious texture, declining with age. | ⚠️ Encorpada e densa (com dextrinas), com uma textura aveludada e deliciosa, diminuindo com a idade. | 17D, 22C |
| 2x | Carbonation may be low to moderate, depending on age and conditioning. | ⚠️ A carbonatação pode ser de baixa a moderada, dependendo da idade e do acondicionamento. | 17D, 22C |
| 2x | Generally quite clear. | Geralmente bastante límpida. | 18B, 19A |
| 2x | Stronger versions may have a slight alcohol warmth. | ⚠️ Versões com teor alcoólico mais alto podem ter um leve aquecimento alcoólico. | 19A, 20A |
| 2x | Should not seem sharp, acrid, or acidic. | ⚠️ Não deve parecer pungente, acre ou ácida. | 20A, 20B |
| 2x | Medium to full body. | ⚠️ Corpo de médio a alto. | 20B, 22B |
| 2x | Can be somewhat creamy. | Pode ser um pouco cremosa. | 20B, 25A |
| 2x | Medium-light to medium body, with a smooth texture. | ⚠️ Corpo de médio-leve a médio, com uma textura suave. | 21A, 22A |
| 2x | Alcohol may be noted, but should not be solventy. | O álcool pode ser notado, mas não deve ser similar a solvente. | 22A, 22B |
| 2x | Neutral or lightly fruity yeast. | Levedura neutra ou levemente frutada. | 22A, 22B |
| 2x | Clarity ranges from clear to somewhat hazy. | ⚠️ A limpidez varia de transparente a um tanto turva. | 23A, 28D |
| 2x | Large, dense, white head with poor retention. | ⚠️ Colarinho branco alto, denso e com retenção pobre. | 23A, 28D |
| 2x | Clean lactic sourness dominates and can be quite strong. | _(a definir)_ | 23A, 28D |
| 2x | Very high carbonation. | Carbonatação muito alta. | 23A, 25B |
| 2x | Average to good head retention. | De média a boa retenção de espuma. | 23B, 23C |
| 2x | Fruited versions should be entered as a 29A Fruit Beer. | ⚠️ Versões com adição de fruta devem ser inscritas como uma 29A Fruit Beer. | 23B, 23C |
| 2x | Belgian brewers consider Flanders Red and Oud Bruin to be of the same style family, but the distinction was first made when Michael Jackson first defined beer styles, since the flavor profiles are distinctly different. | Os cervejeiros belgas consideram a Flanders Red e a Oud Bruin da mesma família de estilos, mas a primeira diferenciação foi feita quando Michael Jackson inicialmente definiu os estilos de cerveja, dado que os perfis de sabor são claramente diferentes. | 23B, 23C |
| 2x | Low alpha acid continental hops. | Lúpulos continentais de baixo alfa ácido. | 23B, 23C |
| 2x | Low spicy-peppery phenols optional. | _(a definir)_ | 23C |
| 2x | Low bready, grainy malt. | _(a definir)_ | 23D, 23E |
| 2x | A noticeable vinegary or cidery character is considered a fault by Belgian brewers. | ⚠️ Um caráter avinagrado ou de cidra perceptível é considerado um defeito pelos cervejeiros belgas. | 23D, 23E |
| 2x | Has a low to high tart, puckering quality without being sharply astringent. | Tem uma acidez de baixa a alta intensidade, trazendo a capacidade de franzir o rosto sem ser acentuadamente adstringente. | 23E, 23F |
| 2x | Medium to medium-light body. | ⚠️ Corpo médio a médio-leve. | X5, 24B |
| 2x | Most commercial examples are in the 6.5 – 7% ABV range. | ⚠️ A maioria dos exemplos comerciais estão na faixa de 6,5 a 7% de ABV. | 25A, 26B |
| 2x | Sourness optional (see Comments). | _(a definir)_ | 25B |
| 2x | Spicy-estery Belgian yeast. | _(a definir)_ | 26B, 26D |
| 2x | Impression of a complex grain bill, although many traditional versions are quite simple, with caramelized sugar syrup or unrefined sugars and yeast providing much of the complexity. | _(a definir)_ | 26B, 26D |
| 2x | Spices not typical; if present, should be subtle. | _(a definir)_ | 26B, 26D |
| 2x | Clarity can be variable; some haze is not a fault. | ⚠️ Limpidez pode variar; turbidez baixa não é necessariamente uma falha. | 28B, 28C |
| 2x | Virtually any style of beer. | Virtualmente qualquer estilo de cerveja. | 28B, 28C |
| 2x | Can also be a blend of styles. | ⚠️ Pode também ser uma mistura de estilos. | 28B, 28C |
| 2x | The Specialty-Type Ingredients should be evident, as well as the defining characteristics of a wild fermentation per the base style. | ⚠️ O ingrediente especial deve ser evidente, assim como as características de uma fermentação selvagem esperadas para o estilo base. | 28C |
| 2x | See the Introduction to Specialty-Type Beer section for additional comments, particularly on evaluating the balance of added ingredients with the base beer. | Veja a introdução da seção Cervejas de Especialidade para comentários adicionais, particularmente sobre a avaliação do equilíbrio dos ingredientes adicionados à cerveja base. | Cat 29, Cat 30 |
| 2x | Lighter-colored beer should show distinctive ingredient colors, including in the head. | Cervejas de cor mais clara, incluindo o colarinho, podem apresentar cores vindas da adição. | 29A, 29B |
| 2x | The color of fruit in beer is often lighter than the flesh of the fruit itself and may take on slightly different shades. | A cor da fruta na cerveja é geralmente mais clara do que a cor da polpa da própria fruta e pode ter tons ligeiramente diferentes. | 29A, 29B |
| 2x | Fruit often decreases body, and makes the beer seem lighter on the palate. | A fruta muitas vezes diminui o corpo e faz a cerveja parecer mais leve no palato. | 29A, 29B |
| 2x | Some smaller and darker fruits may add a tannic depth, but this astringency should not overwhelm the base beer. | Algumas frutas menores e mais escuras podem adicionar uma profundidade tânica, mas essa adstringência não deve sobrepujar a cerveja base. | 29A, 29B |
| 2x | SHVs may increase or decrease body. | ⚠️ Algumas SHVs podem aumentar ou diminuir o corpo. | 29B, 30A |
| 2x | Some SHVs may add a bit of astringency, although a "raw" spice character is undesirable. | ⚠️ Alguns SHVs podem adicionar um pouco de adstringência, ainda que um caráter de especiaria "crua" não seja desejável. | 29B, 30A |
| 2x | Some added sugars will have unfermentable elements that may provide a fuller and sweeter finish; fully fermentable sugars may thin out the finish. | Alguns açúcares adicionados terão elementos não fermentáveis que podem prover um final mais cheio e doce; açúcares totalmente fermentáveis podem deixar o final mais ralo. | 29C, 30D |
| 2x | The entrant must specify the type of additional ingredient (per the introduction) or special process employed. | _(a definir)_ | 29C, 30D |
| 2x | Malty, spicy, and balanced. | Maltado, condimentado e equilibrado. | 30B |
| 2x | The declared ingredients and concept set the expectation. | Os ingredientes declarados e o conceito definem a expectativa. | 30B, 30C |
| 2x | Hops are often subtle. | Lúpulos são geralmente sutis. | 30B, 30C |
| 2x | Alcohol is often present, but smooth and supportive. | Álcool muitas vezes presente, porém suave e de suporte. | 30B, 30C |
| 2x | The components should be well-integrated, and create a coherent presentation. | Os componentes devem estar bem integrados e criar uma apresentação coerente. | 30B, 30C |
| 2x | Well-formed, persistent, off-white to tan head. | Colarinho de boa formação, persistente, de coloração quase branca a bege. | 30B, 30C |
| 2x | Allow for brewer creativity in meeting the theme objective. | _(a definir)_ | 30B, 30C |
| 2x | Warming or sweet spices common. | _(a definir)_ | 30B, 30C |
| 2x | May include distinctive sugar flavors, like molasses, honey, or brown sugar. | _(a definir)_ | 30B, 30C |
| 2x | Age character allowable. | _(a definir)_ | 30B, 30C |
| 2x | Warming alcohol allowable. | _(a definir)_ | 30B, 30C |
| 2x | Malty, spicy, fruity, and balanced. | Maltado, condimentado, frutado e equilibrado. | 30C |
| 2x | Same as base beer style. | O mesmo do estilo base de cerveja. | 31A |
| 2x | The smoke character ranges from low to assertive, and may show varietal wood smoke character (e.g., alder, oak, beechwood). | O caráter defumado varia de baixo a assertivo e pode ter o caráter derivado de vários tipos de madeira (por exemplo, amieiro, carvalho, faia). | 32A, 32B |
| 2x | However, the resulting mix should be appealing. | Entretanto, a combinação resultante deve ser atrativa. | 32A, 32B |
| 2x | Sharp, phenolic, harsh, rubbery, or burnt smoke-derived aromatics are inappropriate. | Aroma acentuado, fenólico, áspero, como borracha ou queimado derivado de defumação é inapropriado. | 32A, 32B |
| 2x | The appearance should reflect the base beer style, although the color is often a bit darker than expected for the plain base style. | A aparência deve refletir o estilo base, embora a cor geralmente seja um pouco mais escura que o esperado para o estilo base sem o defumado. | 32A, 32B |
| 2x | Varietal woods can produce different flavor profiles. | Cada tipo de madeira produz diferentes perfis de sabores. | 32A, 32B |
| 2x | Smoke can add some additional dryness to the finish. | O defumado pode adicionar alguma secura ao final. | 32A, 32B |
| 2x | Harsh, bitter, burnt, charred, rubbery, sulfury, medicinal, or phenolic smoke-derived flavors are inappropriate. | Sabor acentuado, amargo, queimado, carbonizado, como borracha, sulfuroso, medicinal ou fenólico derivado de defumação é inapropriado. | 32A, 32B |
| 2x | Varies with the base beer style. | Varia de acordo com o estilo base da cerveja. | 32A, 32B |
| 2x | Significant astringent, phenolic, smoke-derived harshness is a fault. | Significante aspereza adstringente, fenólica ou derivada de defumação é uma falha. | 32A, 32B |
| 2x | The entrant must specify the type of wood or smoke if a varietal smoke character is noticeable. | _(a definir)_ | 32A, 32B |
| 2x | The best examples will be smooth, flavorful, well-balanced, and well-aged. | Os melhores exemplos serão suaves, saborosos, bem equilibrados e bem envelhecidos. | 33A, 33B |
| 2x | A low to moderate woody aroma is usually present; some varietals may have a stronger, or distinctive character. | Um aroma amadeirado, de baixo a moderado, geralmente está presente; algumas variedades podem ter um caráter mais forte ou distinto. | 33A, 33B |
| 2x | If the wood is toasted or charred, there may be low to moderate vanilla, caramel, toffee, toast, or cocoa character present. | Se a madeira for tostada ou carbonizada, pode haver de baixo a moderado caráter de baunilha, caramelo, toffee, tosta ou cacau. | 33A, 33B |
| 2x | Wood usually contributes a woody flavor, and possibly a distinctive varietal character. | A madeira geralmente contribui com um sabor amadeirado e, possivelmente, com um perfil característico da variedade utilizada. | 33A, 33B |
| 2x | Toasted or charred wood can add vanilla, caramel, butterscotch, toasted bread, toasted nuts, coffee, chocolate, or cocoa, depending on the wood varietal and level of toast or char. | A madeira tostada ou carbonizada pode adicionar notas de baunilha, caramelo, butterscotch, pão tostado, nozes tostadas, café, chocolate ou cacau, dependendo da variedade de madeira e do nível de queima usada. | 33A, 33B |
| 2x | Tannins from the wood may increase the perception of body, as well as enhancing the dryness of the finish; some astringency from wood tannins is allowable. | Os taninos da madeira podem aumentar a percepção de corpo, além de potencializar a secura no final; alguma adstringência dos taninos da madeira é permitida. | 33A, 33B |
| 2x | Tart or acidic characteristics should be low to none, and never distracting. | As características azedas ou ácidas devem ser baixas ou inexistentes, e nunca devem distrair. | 33A, 33B |
| 2x | Age character is allowable, but excessive oxidation or sourness is a fault. | _(a definir)_ | 33A, 33B |
| 2x | Fuller-bodied, higher-gravity base styles often are used since they can best stand up to the additional flavors, although experimentation is encouraged. | Estilos base mais encorpados e de maior densidade geralmente são usados, pois podem resistir melhor aos sabores adicionais, embora experimentações sejam incentivadas. | 33A, 33B |
