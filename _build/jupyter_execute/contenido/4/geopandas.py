#!/usr/bin/env python
# coding: utf-8

# # geopandas: paquete para manipulación y análisis de datos vectoriales

# ## Descripción general

# [Geopandas](http://geopandas.org/) es un proyecto de software libre que extiende los tipos de datos de [pandas](http://pandas.pydata.org/) para incorporar objetos geométricos (puntos, líneas, polígonos, etc), como los utilizados en el modelo vectorial. Se apoya en las bibliotecas [Fiona](https://github.com/Toblerity/Fiona/) para acceder a los datos, [Shapely](https://github.com/Toblerity/Shapely/) para realizar las operaciones geométricas y [matplotlib](https://matplotlib.org/) para graficación.
# 
# Geopandas implementa dos estructuras principales de datos:
# 
# - [GeoSeries](http://geopandas.org/data_structures.html#geoseries): es un vector en el que cada elemento es un conjunto de una o varias geometrías correspondientes a una observación. Por ejemplo, un polígono que representa una provincia, una línea que representa una carretera o un punto que representa una edificación.
# - [GeoDataFrame](http://geopandas.org/data_structures.html#geodataframe): es una estructura tabular (i.e. con filas y columnas) de datos geométricos y no geométricos (ej. textos, números). El conjunto de geometrías se implementa a través de GeoSeries.

# ## Instalación

# Puede instalarse con `pip`, `conda` o `mamba`, desde la línea de comandos del sistema operativo. Solo es necesario hacerlo de una forma.

# ```
# # Con pip:
# pip install geopandas
# 
# # Con conda:
# conda install geopandas -c conda-forge
# 
# # Con mamba:
# mamba install geopandas -c conda-forge
# ```

# ## Carga

# In[1]:


# Carga de la biblioteca pandas con el alias pd
import pandas as pd

# Carga de geopandas
import geopandas as gpd


# In[2]:


# Versión de geopandas
gpd.__version__


# ## Operaciones básicas

# Seguidamente, se describen y ejemplifican algunas de las funciones básicas de geopandas.

# ### read_file() - carga de datos

# In[3]:


# Lectura de datos de países de Natural Earth,
# uno de los conjuntos de datos de ejemplo incluídos en geopandas

paises = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Visualización de los datos
paises


# ### info() - información general sobre un conjunto de datos

# In[4]:


paises.info()


# ### describe() - información estadística

# In[5]:


paises.describe()


# ### head(), tail(), sample() - despliegue de filas de un conjunto de datos

# In[6]:


# Primeros 5 registros
paises.head()


# In[7]:


# Últimos 10 registros
paises.tail(10)


# In[8]:


# 5 registros seleccionados aleatoriamente
paises.sample(5)


# ### Selección de columnas

# Las columnas que se despliegan en un geodataframe pueden especificarse mediante una lista.

# In[9]:


# Despliegue de las columnas con el nombre del país y su población
paises[["name", "pop_est"]]


# ### Selección de filas

# In[10]:


# Países con población estimada mayor o igual a mil millones
paises[paises["pop_est"] >= 1000000000]


# ### Selección de filas y columnas en la misma expresión

# In[11]:


# Columnas de nombre del país y su población 
# para filas con población estimada mayor o igual a mil millones
paises.loc[paises["pop_est"] >= 1000000000, ["name", "pop_est"]]


# ## Operaciones de análisis

# ### plot() - mapeo

# El método [geopandas.GeoDataFrame.plot()](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.plot.html) genera un mapa de un geodataframe mediante `matplotlib`.

# In[12]:


# Mapa básico
paises.plot()


# Si se especifica una columna con el argumento `column`, el mapa se colorea de acuerdo con los valores de esa columna.

# In[13]:


# Mapa de coropletas de la columna
# correspondiente al estimado de población
paises.plot(column = "pop_est", legend=True)


# Mapa de coropletas con una paleta de colores del sitio [ColorBrewer](https://colorbrewer2.org/), creado por [Cynthia Brewer](https://en.wikipedia.org/wiki/Cynthia_Brewer), y un esquema de clasificación basado en [cuantiles](https://es.wikipedia.org/wiki/Cuantil).

# In[14]:


# Mapa de coropletas con paleta de colores y esquema de clasificación
paises.plot(column = "pop_est", 
            legend=True,
            cmap='OrRd', 
            scheme='quantiles',
            figsize=(20, 20)
            )


# Mapa con múltiples capas.

# In[15]:


# Geodataframe de ciudades de Natural Earth
ciudades = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

# Mapa base de países
base = paises.plot(color='white', edgecolor='black', figsize=(20, 20))

# Capa de ciudades
ciudades.plot(ax=base, marker='o', color='red', markersize=8)


# #### Ejercicios

# 1. Descargue del [Sistema Nacional de Información Territorial (SNIT)](https://www.snitcr.go.cr/) las siguientes capas, en el CRS WGS84.
# 
# - Provincias.
# - Cantones.
# - Áreas silvestres protegidas (ASP).
# - Red vial (escala 1:200000).
# 
# 2. Cargue cada capa en un geodataframe.
# 3. Examine la estructura y el contenido de cada conjunto de datos.
# 4. Despliegue algunos mapas para cada capa, utilizando las funciones de matplotlib y geopandas.
# 5. Genere mapas que presenten la capa de red vial con las otras tres.

# ## Ejemplo de análisis: distribución de murciélagos en ASP de Costa Rica

# En los siguientes ejemplos, se utilizará un conjunto de registros de presencia de murciélagos (orden *Chiroptera*) de Costa Rica, en formato CSV, obtenido a través de una [consulta al portal de la Infraestructura de Información Mundial en Biodiversidad (GBIF)](https://doi.org/10.15468/dl.g5ce3g). También se utilizará la capa de ASP del Sistema Nacional de Áreas Protegidas de Costa Rica (Sinac).
# 
# Como resultado, se obtiene un mapa que muestra la cantida de especies de murciélagos en cada ASP.

# ### Carga de datos

# #### Murciélagos

# Ya que los archivos de valores separados por comas (CSV) no tienen un formato geoespacial (SHP, GPKG, GeoJSON u otro), los datos de murciélagos se cargan primero en un dataframe normal (i.e. sin geometrías).

# In[16]:


# Carga de registros de presencia de murciélagos en un dataframe
murcielagos = pd.read_csv("datos/gbif/murcielagos.csv", sep="\t")

# Despliegue de los datos
murcielagos


# Luego, con el método [geopandas.points_from_xy()](https://geopandas.org/en/stable/docs/reference/api/geopandas.points_from_xy.html), se crea una columna de geometrías de puntos, con base en las columnas `decimalLongitude` y `decimalLatitude`.

# In[17]:


# Geodataframe creado a partir del dataframe
murcielagos = gpd.GeoDataFrame(murcielagos, 
                               geometry=gpd.points_from_xy(murcielagos.decimalLongitude, 
                                                           murcielagos.decimalLatitude),
                               crs="EPSG:4326")

# Despliegue de los datos (incluyendo geometrías)
murcielagos


# Ahora que los datos de murciélagos están en un geodataframe, pueden desplegarse en un mapa.

# In[18]:


# Mapa
murcielagos.plot(figsize=(20, 20))


# #### Áreas silvestres protegidas (ASP)

# Como los datos de ASP sí están en un formato geoespacial (ej. GeoJSON), pueden cargarse directamente en un geodataframe.

# In[19]:


# Carga de polígonos de ASP
asp = gpd.read_file("datos/sinac/asp.geojson", sep="\t")

# Despliegue tabular de los datos
asp


# In[20]:


# Mapa de ASP
asp.plot(figsize=(20, 20))


# Ahora, ambas capas pueden mostrarse en un mismo mapa.

# In[21]:


# Capa base de países
base = asp.plot(color='white', edgecolor='black', figsize=(20, 20))

# Capa de murciélagos
murcielagos.plot(ax=base, marker='o', color='red', markersize=8)


# ### Conteo de especies en cada ASP

# Con el método [geopandas.sjoin()](https://geopandas.org/en/stable/docs/reference/api/geopandas.sjoin.html), se realiza una [unión espacial o *spatial join*](https://gisgeography.com/spatial-join/) de las tablas de ASP y de murciélagos. Esto produce un geodataframe con una fila por cada registro de murciélagos, la cual contiene también la información del ASP en donde se ubica el registro. 
# 
# En este caso, se conservan solo las filas en donde hay intersección de las geometrías de ambas tablas. O sea, aquellos registros de murciélagos que se ubican en un ASP. Se excluyen los registros ubicados fuera de las ASP.

# In[22]:


# Join espacial de las capas de ASP y murciélagos
asp_murcielagos = asp.sjoin(murcielagos)

asp_murcielagos


# In[23]:


# Estructura
asp_murcielagos.info()


# In[24]:


# Mapa de ASP en las que hay registros de murciélagos
asp_murcielagos.plot(figsize=(20, 20))


# Seguidamente, se cuenta la cantidad de especies que hay en cada ASP.

# In[25]:


# Conteo de especies en cada ASP
conteo_asp_especies = asp_murcielagos.groupby("nombre_asp").species.nunique()
conteo_asp_especies = conteo_asp_especies.reset_index() # para convertir la serie a dataframe

# Cambio de nombre de columna
conteo_asp_especies.rename(columns = {'species': 'especies'}, inplace = True)

# Despliegue de ASP por cantidad de especies
conteo_asp_especies.sort_values(by="especies", ascending=False)


# El método [pandas.DataFrame.join()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html) se usa seguidamente para unir el geodataframe de ASP con el dataframe que contiene el conteo de especies por ASP. Como resultado, el geodataframe de ASP tiene ahora la columna con la cantidad de especies.

# In[26]:


# Join para agregar la columna con el conteo a la capa de ASP
asp_especies = asp.join(conteo_asp_especies.set_index('nombre_asp'), on='nombre_asp')
asp_especies


# In[27]:


# Mapeo
asp_especies.plot(column="especies", 
            legend=True,
            cmap='OrRd', 
            scheme='quantiles',
            figsize=(20, 20)
            )


# ## Ejercicios

# Desarrolle los siguientes mapas, primero en QGIS y luego en Python con las funciones de la biblioteca GeoPandas.
# 
# 1. Mapa de coropletas que muestre la cantidad de casos positivos de COVID en cantones de Costa Rica.
# 2. Mapa de coropletas que muestre la cantidad de casos positivos de COVID en provincias de Costa Rica.
# 
# 3. Mapa de coropletas que muestre la cantidad de especies de murciélagos en cantones de Costa Rica.
# 4. Mapa de coropletas que muestre la cantidad de especies de murciélagos en provincias de Costa Rica.
# 
# 5. Mapa de coropletas que muestre la densidad de la red vial ( * ) en cantones de Costa Rica ( ** ).
# 6. Mapa de coropletas que muestre la densidad de la red vial ( * ) en provincias de Costa Rica.
# 
# Además de los mapas, visualice los resultados en tablas y gráficos, cuando le ayuden a verificar o comprender mejor el problema a resolver.
# 
# ( * ) La densidad de la red vial para un polígono se define como:  
# **km de longitud de red vial / km2 de área**  
# Por ejemplo, si un cantón tiene 500 km de longitud de red vial y un área de 1000 km2, la densidad de su red vial es 0.5.
# 
# ( ** ) Puede encontrar una solución al problema del cálculo de la densidad de la red vial en [https://github.com/gf0657-programacionsig/2022-ii-densidad-redvial](https://github.com/gf0657-programacionsig/2022-ii-densidad-redvial).

# ## Recursos de interés

# **Unión (*join*) de datos**
# - [How To Think Spatially with Spatial Relationships](https://gisgeography.com/spatial-relationships/)
# - [GeoPandas - Merging Data](https://geopandas.org/en/stable/docs/user_guide/mergingdata.html)
# - [Geopandas - Spatial Joins](https://geopandas.org/en/stable/gallery/spatial_joins.html)
# 
# **Agrupación de datos**
# - [pandas GroupBy: Your Guide to Grouping Data in Python](https://realpython.com/pandas-groupby/)
# - [pandas.DataFrame.groupby](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)
# 
# **Superposición (*overlay*) de datos**  
# - [geopandas.overlay](https://geopandas.org/en/stable/docs/reference/api/geopandas.overlay.html)

# In[ ]:




