# Tarea 03

## Fecha y hora límite de entrega
Jueves 24 de noviembre de 2022, 05:59 a.m.

## Objetivos
Cada estudiante debe mostrar que es capaz de:

1. Desarrollar programas en Python como cuadernos de notas de Jupyter (*Jupyter notebooks*).
2. Manejar datos con las bibliotecas Pandas y GeoPandas.
3. Implementar tablas, gráficos y mapas interactivos con las bibliotecas Plotly y Folium.
4. Publicar resultados en la Web, junto con el código y los datos que los generan.

## Entregables
Dirección de un repositorio en GitHub que contenga código, datos y documentación. Específicamente:

1. Un cuaderno de notas de Jupyter con el código Python necesario para generar las salidas especificadas en la sección de desarrollo.
2. Un directorio con archivos de datos.
3. Un archivo `README.md` con:
    1. Una breve descripción (no mayor a 200 palabras) del contenido del repositorio. Si lo desea, puede incluir su interpretación de los resultados.
    2. Una mención y un enlace a la fuente de los datos.
    3. Un enlace al sitio [NBViewer](https://nbviewer.org/) con la visualización del cuaderno de notas con las tablas y gráficos. También puede entregarse un enlace a un cuaderno de notas en [Google Colab](https://colab.research.google.com/). Si se utiliza esta última opción, debe compartirse el cuaderno con mfvargas@gmail.com (con derechos para visualizarlo).

La entrega debe realizarse a través de la plataforma Mediación Virtual.

## Consideraciones adicionales
Esta tarea puede realizarse en parejas o de manera individual. Si es en pareja, solo un integrante debe realizar la entrega e indicar el nombre del otro integrante en Mediación Virtual.

## Desarrollo
Debe desarrollar un programa en Python, como un cuaderno de notas de Jupyter, que utilice los siguientes conjuntos de datos:

- [Registros de presencia de felinos de Costa Rica, agrupados por la Infraestructura Mundial de Información en Biodiversidad (GBIF)](https://doi.org/10.15468/dl.dwpgps).
- [Áreas silvestres protegidas (ASP) de Costa Rica, publicadas por el Sistema Nacional de Áreas de Conservación (Sinac) en el Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/ico_servicios_ogc_info?k=bm9kbzo6NDA=&nombre=SINAC).
- [Capa raster de WorldClim de altitud de Costa Rica en resolución de 30 x 30 segundos](https://github.com/gf0657-programacionsig/2022-ii/blob/main/contenido/4/datos/worldclim/altitud.tif). ([Enlace al sitio de WorldClim](https://www.worldclim.org/)).

Debe cargar los datos con Python y prepararlos mediante:

- Conversiones de tipos (ej. fechas).
- Eliminación de columnas no necesarias.
- Eliminación de filas no necesarias.
- Cambio de nombres de columnas.

Luego, debe implementar las siguientes salidas:

1.  Una tabla que muestre los registros de presencia de felinos. Incluya las columnas: especie (`species`), provincia (`stateProvince`), localidad (`locality`), fecha (`eventDate`).

2.  Un gráfico *sunburst* que muestre las cantidades de registros de presencia por género (nivel interior) y por especie (nivel exterior).

3.  Un mapa que muestre las siguientes cinco capas:

-   Dos capas base (ej. OpenStreetMap).
-   Capa raster de altitud de Costa Rica.
-   Capa de polígonos de ASP de Costa Rica. La ventana emergente (*popup*) debe mostrar el nombre del ASP al hacer clic sobre el polígono.
-   Capa de puntos de registros de presencia de felinos. La ventana emergente (*popup*) debe mostrar el nombre de la especie, la provincia, la localidad y la fecha.


Considere este proyecto como un breve artículo de análisis de datos y siga los siguientes lineamientos:

- El código en Python y sus salidas deben ser **legibles y bien presentados**. 
- Procure incluir solamente el código necesario para generar los resultados.
- Agregue texto en Markdown para darle estructura al cuaderno de notas e incluir las explicaciones que considere necesarias.
- El mapa tener un control de capas.

## Calificación
Entre paréntesis, se muestra el porcentaje correspondiente a cada aspecto que se calificará:

-   Estructura y legibilidad del cuaderno de notas (10%).
-   Inclusión de los archivos de datos en el repositorio (5%).
-   Inclusión del archivo `README.md`, con el contenido descrito en la sección Entregables (5%).
-   Preparación de los archivos de datos (5%).
-   Tabla con registros de presencia de especies (10%).
-   Gráfico *sunburst* (30%).
-   Mapa (35%).
