# Interactive Map Classes

Este repositório contém duas classes para criar mapas interativos usando Python e a biblioteca Cartopy. As classes permitem selecionar uma área ou ponto no mapa através de eventos de clique do mouse.


## SelAreaMap

A classe `SelAreaMap` permite criar um mapa interativo de uma região específica, definida pelos limites de latitude e longitude. Esta classe possui um evento de clique no mapa que permite ao usuário selecionar uma área retangular e salvar uma figura da região selecionada. 

### Uso

```python
from ocean-point import SelAreaMap

dataset_path = "../data/ETOPO1_Bed_g_gmt4.grd"

Escolha uma região: ['nordeste','sudeste','sul']

region = 'sudeste'
mapa = SelPointMap(dataset_path, region)


## SelAreaMap

A classe `SelPointMap` permite criar um mapa interativo que exibe a batimetria de uma região. Esta classe possui um evento de clique no mapa que permite ao usuário selecionar um ponto e exibir as coordenadas de latitude e longitude do ponto selecionado. Além disso, o mapa com o ponto selecionado é salvo como uma imagem.

### Uso

```python
from ocean-point import SelPointMap

mapa = SelPointMap('"../data/ETOPO1_Bed_g_gmt4.grd"', region='sudeste')


