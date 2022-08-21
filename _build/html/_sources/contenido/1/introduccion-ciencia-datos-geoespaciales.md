# Introducción a la ciencia de datos geoespaciales


## Trabajo previo

### Lecturas
Hwang, J. P. (2021, septiembre 3). Building a Big Data Geographical Dashboard with Open-Source Tools. Plotly. https://medium.com/plotly/building-a-big-data-geographical-dashboard-with-open-source-tools-c5108d7d5683

Rey, S. J., Arribas-Bel, D., & Wolf, L. J. (2020). Geographic Data Science with Python. https://geographicdata.science/book/ (Parte I)

Wu, Q. (2021, octubre 25). A streamlit app for creating timelapse of annual Landsat imagery (1984–2021). Medium. https://giswqs.medium.com/a-streamlit-app-for-creating-timelapse-of-annual-landsat-imagery-1984-2021-3db407a8ac32


## El componente geoespacial de los datos
Una gran parte de los datos disponibles contiene algún tipo de componente geográfico o espacial[^footnote-geografico-espacial]. Este componente puede expresarse de varias formas. Por ejemplo:

- **Con nombres de lugares**: *El [sapo dorado (*Incilius periglenes*)](https://es.wikipedia.org/wiki/Incilius_periglenes) era una especie de anfibio, endémica de los bosques nubosos de altitud de Monteverde, Costa Rica.*
- **Con direcciones**: *La [sede de la Organización de las Naciones Unidas (ONU)](https://es.wikipedia.org/wiki/Sede_de_la_Organizaci%C3%B3n_de_las_Naciones_Unidas) está ubicada en la ciudad de Nueva York, Estados Unidos, en la Primera Avenida, 750.*
- **Con coordenadas**: *La cima del [Monte Everest](https://es.wikipedia.org/wiki/Monte_Everest) se localiza en las coordenadas geográficas 86°55′31″ E y 27°59′17″ N, como se muestra en la {numref}`figure-mapa-nepal-everest`.

```{figure} img/nepal-map.jpg
:name: figure-mapa-nepal-everest

Mapa de Nepal que muestra la ubicación del Monte Everest en el sistema de coordenadas geográficas. Fuente: [https://www.mapsofworld.com/](https://www.mapsofworld.com/).
```

Las coordenadas correspondientes a lugares y direcciones pueden obtenerse a través de un proceso denominado [*georreferenciación*](https://es.wikipedia.org/wiki/Georreferenciaci%C3%B3n), mediante el cual, en general, se determina la posición espacial de alguna entidad en un sistema de coordenadas. La georreferenciación puede emplearse también para obtener las coordenadas de, por ejemplo, fotografías aéreas o mapas antiguos. Es un proceso que puede resultar complejo y costoso y para el que se han desarrollado metodologías y plataformas especializadas (ej. [Chapman AD & Wieczorek JR (2020) Georeferencing Best Practices](https://doi.org/10.15468/doc-gg7h-s853), [GEOLocate](https://www.geo-locate.org/), [Nominatim](https://nominatim.openstreetmap.org/ui/search.html)).

En la actualidad, hay una gran cantidad de fuentes que generan datos georreferenciados. Entre estas pueden mencionarse las tecnologías de [observación de la Tierra (*Earth Observation*)](https://ec.europa.eu/jrc/en/research-topic/earth-observation) (ej. [imágenes satelitales](https://es.wikipedia.org/wiki/Imagen_satelital)), los dispositivos móviles y los sensores remotos, entre muchas otras.

## Sistemas de información geográfica
A principios de la década de 1960, el geógrafo inglés [Roger Tomlinson](https://es.wikipedia.org/wiki/Roger_Tomlinson) desarrolló en Canadá el que se considera el primer sistema de información geográfica. Se trataba del [Canada Geographic Information System (CGIS)](https://en.wikipedia.org/wiki/Canada_Geographic_Information_System) y su objetivo fue manejar los datos del inventario geográfico canadiense y su análisis para la gestión del territorio rural. De manera casi simultánea al trabajo de Tomlinson, surgieron desarrollos similares en Estados Unidos y en el Reino Unido. El surgimiento de los sistemas de información geográfica no implicó solo el surgimiento de nuevas herramientas de software, sino también el desarrollo de técnicas que hasta entonces no habían sido necesarias {cite}`olaya_sistemas_2020` como, por ejemplo, la manipulación de nuevos tipos de datos geométricos (ej. puntos, líneas, polígonos).

En general, un sistema de información geográfica (SIG) maneja datos georreferenciados (i.e. ubicados en un sistema de coordenadas) y los asocia con datos convencionales, como se muestra en la {numref}`figure-mapa-qgis`.

```{figure} img/mapa-qgis.png
:name: figure-mapa-qgis

Mapa elaborado en QGIS que muestra la ubicación de los aeródromos de Costa Rica.
```

En la actualidad, los SIG presentan los datos en capas (*layers*). Por ejemplo, el mapa de la {numref}`figure-mapa-qgis` contiene una capa base raster (la que muestra el mar y el continente), una capa de polígonos correspondiente a las provincias de Costa Rica y una capa de puntos correspondiente a los aeródromos. A la izquierda puede apreciarse la lista de esas capas y a la derecha un cuadro con información detallada sobre uno de los aeródromos.

Los SIG de escritorio (ej. [ArcGIS Desktop](https://www.esri.com/en-us/arcgis/products/arcgis-desktop/overview), [QGIS](https://www.qgis.org/)) son herramientas con interfaces de usuario muy gráficas e intuitivas, que no requieren de conocimientos de programación de computadoras y que permiten generar cartografía de alta calidad. Sin embargo, son poco flexibles y los resultados que producen son difícilmente [reproducibles](https://es.wikipedia.org/wiki/Reproducibilidad_y_repetibilidad).

## El enfoque de ciencia de datos geoespaciales
Durante la última década, el uso de SIG se ha complementado con el de [ciencia de datos](https://es.wikipedia.org/wiki/Ciencia_de_datos), lo que posibilitado enriquecer la visualización y el análisis de datos geoespaciales mediante lenguajes de programación como [Python](https://www.python.org/), [R](https://www.r-project.org/) o [JavaScript](http://www.ecma-international.org/publications-and-standards/standards/ecma-262/), entre otros.

El uso de técnicas de ciencia de datos y de otros campos relacionados (ej. [aprendizaje automatizado](https://es.wikipedia.org/wiki/Aprendizaje_autom%C3%A1tico), [*big data*](https://es.wikipedia.org/wiki/Macrodatos)) ha permitido aplicar a los datos geoespaciales técnicas y metodologías como [análisis de regresión](https://es.wikipedia.org/wiki/An%C3%A1lisis_de_la_regresi%C3%B3n) y [clasificación estadística](https://es.wikipedia.org/wiki/Clasificaci%C3%B3n_estad%C3%ADstica).

## Referencias bibliográficas
```{bibliography}
:filter: docname in docnames
```

[^footnote-geografico-espacial]: El adjetivo *geográfico* se refiere a la superficie de la Tierra. Así, por ejemplo, las *coordenadas geográficas* se utilizan para ubicar cualquier punto en la superficie terrestre. El término *espacial* se emplea para referirse a cualquier espacio, no siempre localizable en el planeta Tierra. En muchas ocasiones, ambas palabras son intercambiables. Por ejemplo, muchos de los métodos utilizados para analizar datos geográficos pueden aplicarse también en espacios no geográficos como, por ejemplo, otros planetas, el cosmos, el cuerpo humano (ej. con radiografías) o secuencias genómicas. En los últimos años, se ha incrementado el uso del término *geoespacial*, el cual se eligió para el nombre de este curso, como una forma de referirse al subconjunto del espacio correspondiente a la superficie de la Tierra {cite}`longley_geographic_2005`.