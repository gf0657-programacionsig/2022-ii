# Proyecto final

## Fecha y hora límite de entrega
Lunes 12 de diciembre de 2022, 11:59 p.m.

## Objetivos
Cada estudiante debe mostrar que es capaz de:

1. Manejar datos con las bibliotecas Pandas y GeoPandas.
2. Implementar tablas, gráficos y mapas interactivos con las bibliotecas Plotly y Folium.
3. Desarrollar aplicaciones interactivas con la biblioteca Streamlit y publicarlas en la plataforma Streamlit Cloud.

## Entregables
Dirección de un repositorio en GitHub que contenga el código, los datos, la documentación y la dirección web de una aplicación Streamlit que permita visualizar datos de registros de presencia de especies mediante tablas, gráficos y mapas. Específicamente, debe entregarse:

1. El código fuente de la aplicación.
2. Un directorio con archivos de datos.
3. Un archivo `README.md` con:
    1. Una breve descripción (no mayor a 200 palabras) del contenido del repositorio. Si lo desea, puede incluir su interpretación de los resultados.
    2. Una mención y un enlace a la fuente de los datos (ej. fuente de los datos geoespaciales).
    3. Un enlace a la aplicación Streamlit publicada en Streamlit Cloud.

La entrega debe realizarse a través de la plataforma Mediación Virtual.

## Consideraciones adicionales
Esta tarea puede realizarse en parejas o de manera individual. Si es en pareja, solo un integrante debe realizar la entrega e indicar el nombre del otro integrante en Mediación Virtual.

## Desarrollo

### Conjuntos de datos de entrada
1. Un archivo CSV con registros de presencia de especies de Costa Rica, que seleccione el usuario, que siga el estándar [Darwin Core (DwC)](https://dwc.tdwg.org/terms/). Este tipo de archivos puede obtenerse en el portal de la Infraestructura Mundial de Información en Biodiversidad (GBIF) ([https://www.gbif.org/occurrence/search](https://www.gbif.org/occurrence/search)). Ejemplos:
    - [Registros de presencia de felinos de Costa Rica](datos/felinos.csv)
    - [Registros de presencia de murciélagos de Costa Rica](datos/murcielagos.csv)

2. Un archivo GeoJSON con [polígonos de cantones de Costa Rica, publicados por el Instituto Geográfico Nacional (IGN) en el Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/ico_servicios_ogc_info?k=bm9kbzo6MjY=&nombre=IGN%20Cartograf%C3%ADa%201:5mil).


### Controles de entrada
1. Un botón para solicitarle al usuario el archivo CSV con registros de presencia.

2. Una lista de selección con los nombres de las especies contenidos en el archivo CSV. La tabla, los gráficos y el mapa deben mostrar los datos de la especie que seleccione el usuario.

### Salidas
1.  Una tabla que muestre los registros de presencia de la especie seleccionada. 
    - Incluya las columnas: especie (`species`), provincia (`stateProvince`), localidad (`locality`), fecha (`eventDate`).

2. Un gráfico plotly de barras que muestre la cantidad de registros de la especie seleccionada en cada provincia de Costa Rica en la que haya al menos un registro.
    - El gráfico debe tener título, etiqueta para el eje X y etiqueta para el eje Y.
    - Las barras deben estar ordenadas según su longitud.
    
3. Un gráfico plotly de barras que muestre la cantidad de registros de la especie seleccionada en cada cantón de Costa Rica en el que haya al menos un registro.
    - El gráfico debe tener título, etiqueta para el eje X y etiqueta para el eje Y.
    - Las barras deben estar ordenadas según su longitud.

4.  Un mapa folium con:
-   Dos capas base (ej. OpenStreetMap).
-   Una capa de coropletas que muestre la cantidad de registros de la especie seleccionada en provincias de Costa Rica.
-   Una capa de coropletas que muestre la cantidad de registros de la especie seleccionada en cantones de Costa Rica.
-   Una capa de puntos agrupados correspondientes a los registros de presencia de la especie seleccionada. La ventana emergente (*popup*) debe mostrar el nombre de la especie, la provincia, el cantón y la fecha.
-   Un control para activar y desactivar las capas.


## Calificación
Entre paréntesis, se muestra el porcentaje correspondiente a cada aspecto que se calificará:

-   Estructura y legibilidad del código fuente (5%).
-   Inclusión de los archivos de datos en el repositorio (5%).
-   Inclusión del archivo `README.md`, con el contenido descrito en la sección Entregables (5%).
-   Preparación de los archivos de datos (5%).
-   Botón para seleccionar el archivo de registros de presencia (10%).
-   Lista de selección de especies (10%)
-   Tabla con registros de presencia de especies (5%).
-   Gráfico de barras de provincias (15%).
-   Gráfico de barras de cantones (15%).
-   Mapa (25%).
