# Ocean Point

Este repositório contém duas classes para criar mapas interativos usando Python e a biblioteca Cartopy. As classes permitem selecionar uma área ou ponto no mapa através de eventos de clique do mouse. Selecionar ponto (lon, lat) ou área (lon_min, lon_max, lat_min, lat_max).

A ideia é facilitar a aquisição das coordenadas lat e lon de um ponto ou uma área, para uso na seleção de dados meteoceanográficos. 

Essa rotina é parte das rotinas que uso para desenvolvimento da minha dissertação de mestrado. 


## SelAreaMap

A classe `SelAreaMap` permite criar um mapa interativo de uma região específica, definida pelos limites de latitude e longitude. Esta classe possui um evento de clique no mapa que permite ao usuário selecionar uma área retangular e salvar uma figura da região selecionada. 

### Uso

```python
from ocean-point import SelAreaMap

dataset_path = "../data/ETOPO1_Bed_g_gmt4.grd"

# Escolha uma região: ['nordeste','sudeste','sul']

region = 'sudeste'
mapa = SelAreaMap(dataset_path, region)
```

## SelPointMap

A classe `SelPointMap` permite criar um mapa interativo que exibe a batimetria de uma região. Esta classe possui um evento de clique no mapa que permite ao usuário selecionar um ponto e exibir as coordenadas de latitude e longitude do ponto selecionado. Além disso, o mapa com o ponto selecionado é salvo como uma imagem.

### Uso

```python
from ocean-point import SelPointMap

mapa = SelPointMap('"../data/ETOPO1_Bed_g_gmt4.grd"', region='sudeste')
```

Para utilizar as classes, siga os passos abaixo:

- Instale as dependências necessárias, como Cartopy, Matplotlib, xarray e outras mencionadas no código.
- Faça o download do arquivo de dados da batimetria e coloque-o no diretório indicado.
- Adapte os exemplos de uso fornecidos para as classes SelAreaMap e SelPointMap de acordo com suas necessidades e  regiões de interesse.
- Execute o script Python e interaja com o mapa gerado para selecionar a área ou o ponto desejado

## To do

- Traduzir tudo para inglês
- Salvar lat e lon em um .csv ou .txt
- Problema com o arquivo da batimetria muito pesado (talvez baixar na hora de acordo com a solicitação do usuário)

Essa é minha primeira tentativa de disponibilizar um pacote para outros oceanógrafos... sugestões são bem vindas! :)
