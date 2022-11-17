#!/usr/bin/env python
# coding: utf-8

# # Manejo de datos raster

# ## Descripción general

# En este capítulo, se muestran ejemplos de manejo de datos raster con Python.
# 
# Los datos se obtienen de servicios basados en la especificación [SpatioTemporal Asset Catalogs (STAC)](https://stacspec.org), la cual proporciona una estructura común para describir y catalogar recursos espacio temporales (ej. imágenes satelitales) a través de una interfaz de programación de aplicaciones (en inglés, [API o *Application Programming Interface*](https://es.wikipedia.org/wiki/Interfaz_de_programaci%C3%B3n_de_aplicaciones)). Puede explorar catálogos y API de tipo STAC en el sitio web [STAC browser](https://radiantearth.github.io/stac-browser/).

# ## Instalación de módulos

# Algunos de los módulos que se utilizan en este capítulo son:
# 
# - [rasterio](https://rasterio.readthedocs.io/): para operaciones generales de manejo de datos raster.
# - [xarray](https://docs.xarray.dev/): para manejo de arreglos multidimensionales.
# - [rioxarray](https://corteva.github.io/rioxarray/stable/): extensión de xarray para trabajar con rasterio. 
# - [pystac_client](https://pystac-client.readthedocs.io/): para trabajar con catálogos STAC.

# ```
# # Instalación, mediante mamba, de módulos para manejo de datos raster y acceso a recursos STAC
# mamba install -c conda-forge xarray rioxarray earthpy xarray-spatial pystac-client python-graphviz
# ```

# ## Lectura

# ### Acceso a recursos STAC

# In[1]:


# Carga de pystac_client, para acceder datos en STAC
from pystac_client import Client


# Se accede el API de [Earth Search](https://radiantearth.github.io/stac-browser/#/external/earth-search.aws.element84.com/v0), el cual proporciona acceso a conjuntos de datos públicos en Amazon Web Services (AWS).
# 
# La función [Client.open()](https://pystac-client.readthedocs.io/en/stable/api.html#pystac_client.Client.open) retorna un objeto tipo `Client`, el cual se utiliza para acceder el API (ej. realizar búsquedas). 

# In[2]:


# URL del API STAC
api_url = "https://earth-search.aws.element84.com/v0"

# Cliente para acceso a los datos
client = Client.open(api_url)


# En este ejemplo, se accederá una colección de imágenes Sentinel en formato [Cloud Optimized GeoTIFF (COG)](https://www.cogeo.org/).

# In[3]:


# Colección
collection = "sentinel-s2-l2a-cogs"


# Se especifica un punto (x, y) para buscar imágenes que lo contengan.

# In[4]:


# Punto para búsqueda
from shapely.geometry import Point
point = Point(-84, 10)


# La función [Client.search()](https://pystac-client.readthedocs.io/en/stable/api.html#pystac_client.Client.search) realiza una búsqueda con base en criterios como colección e intersección.

# In[5]:


# Búsqueda de items (imágenes) que contienen el punto
search = client.search(collections=[collection],
                       intersects=point,
                       max_items=10,
)


# In[6]:


# Cantidad total de items que retorna la búsqueda
search.matched()


# In[7]:


# Items retornados
items = search.get_all_items()

len(items)


# In[8]:


# Identificadores de los items retornados
for item in items:
    print(item)


# Para estudiarlo en detalle, se selecciona un item.

# In[9]:


# Primer item (imagen) retornado
item = items[0]


# **Nótese que al seleccionarse el item mediante una posición en una colección, la imagen correspondiente puede cambiar si se actualizan los datos del API**.

# In[10]:


# Algunos atributos del item
print(item.id)
print(item.datetime)
print(item.geometry)
print(item.properties)


# Ahora, se realiza la búsqueda con base en un rectángulo delimitador (*bounding box*) generado a partir del punto que se definió anteriormente.

# In[11]:


# Rectángulo para búsquedas
bbox = point.buffer(0.01).bounds
bbox


# También se restringe la búsqueda para retornar solo aquellas imágenes con cobertura de nubes menor al 10%.

# In[12]:


# Búsqueda con nuevos criterios
search = client.search(collections=[collection],
                       bbox=bbox,
                       datetime="2022-01-01/2022-10-30",
                       query=["eo:cloud_cover<10"]) # no deben haber espacios alrededor del '<'

# Cantidad total de items que retorna la búsqueda
search.matched()


# In[13]:


# Items retornados
items = search.get_all_items()

len(items)


# In[14]:


# Segundo item retornado y algunos de sus atributos
item = items[1]

print(item.datetime)
print(item.properties)


# #### Ejercicio
# 
# Realice el [ejercicio de búsqueda de imágenes Landsat 8](https://carpentries-incubator.github.io/geospatial-python/05-access-data/index.html#exercise-downloading-landsat-8-assets) del curso [The Carpentries Incubator - Introduction to Geospatial Raster and Vector Data with Python](https://carpentries-incubator.github.io/geospatial-python/). Puede cambiar el punto de la búsqueda por otro que sea de su interés.

# In[15]:


# URL del API STAC
api_url_landsat = "https://cmr.earthdata.nasa.gov/stac/LPCLOUD"

# Cliente para acceso a los datos
client_landsat = Client.open(api_url_landsat)


collection_landsat = "HLSL30.v2.0"

point_landsat = Point(-84, 10)

search_landsat = client_landsat.search(collections=[collection_landsat], 
                                       intersects=point_landsat)

search_landsat.matched()


# In[16]:


items_landsat = search_landsat.get_all_items()

len(items_landsat)


# In[17]:


i = 0

for item_landsat in items_landsat:
    if (item_landsat.properties["eo:cloud_cover"] < 20):
        print(i, item_landsat.id, item_landsat.properties["eo:cloud_cover"])
    i += 1


# In[18]:


item_landsat = items_landsat[188]
item_landsat


# In[19]:


print(item_landsat.datetime)
print(item_landsat.properties)


# In[20]:


item_landsat.assets


# In[21]:


assets_landsat = item_landsat.assets


# In[22]:


assets_landsat.keys()


# In[23]:


# Nombres de los activos
for key, asset in assets_landsat.items():
    print(f"{key}: {asset.title}")


# In[24]:


import rioxarray


# In[25]:


# Vista general de la imagen (True Color)
browse = rioxarray.open_rasterio(item_landsat.assets['browse'].href)

browse


# In[26]:


browse.shape


# In[27]:


browse.plot.imshow()


# In[28]:


import os
os.environ["GDAL_HTTP_COOKIEFILE"] = "./cookies.txt"
os.environ["GDAL_HTTP_COOKIEJAR"] = "./cookies.txt"


# In[29]:


# Banda 4
b_04 = rioxarray.open_rasterio(assets_landsat["B04"].href)

b_04


# In[30]:


b_04.plot(robust=True)


# In[31]:


# Bandas necesarias para el cálculo
b_red = rioxarray.open_rasterio(assets_landsat["B04"].href)
b_nir = rioxarray.open_rasterio(assets_landsat["B05"].href)


# In[32]:


# Dimensiones de las bandas
print(b_red.shape, b_nir.shape)


# In[33]:


# Cálculo del NDVI
ndvi = (b_nir - b_red)/ (b_nir + b_red)


# In[59]:


# Visualización del cálculo del NDVI
ndvi.plot(robust=True)


# In[60]:


ndvi.rio.to_raster("ndvi_landsat.tif")


# ### *Assets*

# Cada item retornado contiene un conjunto de "activos" (*assets*) (ej. bandas) que también pueden accederse mediante el API.

# In[ ]:


# Activos (assets) del item
assets = item.assets

# Llaves
assets.keys()


# In[ ]:


# Contenido completo de los items
assets.items()


# In[ ]:


# Nombres de los activos
for key, asset in assets.items():
    print(f"{key}: {asset.title}")


# In[ ]:


# Imagen thumbnail
assets["thumbnail"]


# In[ ]:


# URL del thumbnail
assets["thumbnail"].href


# ## Visualización

# In[ ]:


# Carga de rioxarray, para graficar datos raster
import rioxarray


# El módulo rioxarray provee un conjunto de funciones para manipular imágenes.
# 
# Las bandas pueden abrirse con la función [open_rasterio()](https://corteva.github.io/rioxarray/html/rioxarray.html#rioxarray-open-rasterio) y graficarse con [plot()](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.plot.html#xarray.DataArray.plot) y [plot.imshow()](https://docs.xarray.dev/en/stable/generated/xarray.DataArray.plot.imshow.html).

# #### Visualización del `overview`

# El `overview` es una imagen de tres bandas tipo "True Color".

# In[ ]:


# Vista general de la imagen (True Color)
overview = rioxarray.open_rasterio(item.assets['overview'].href)

overview


# In[ ]:


# Dimensiones de la imagen (bandas, filas, columnas)
overview.shape


# In[ ]:


# Graficación de imagen RGB
overview.plot.imshow(figsize=(8, 8))


# #### Visualización de una banda

# In[ ]:


# Banda 9
b_09 = rioxarray.open_rasterio(assets["B09"].href)

b_09


# In[ ]:


# Graficación de la banda
# robust=True calcula el rango de colores entre los percentiles 2 y 98
b_09.plot(robust=True)


# ## Ejemplo de álgebra raster: cálculo del NDVI

# Seguidamente, se utiliza la imagen Sentinel para calcular el [Índice de vegetación de diferencia normalizada (NDVI)](https://es.wikipedia.org/wiki/%C3%8Dndice_de_vegetaci%C3%B3n_de_diferencia_normalizada).

# Se separan las dos bandas necesarias para el cálculo: la roja y la infrarroja cercana.

# In[ ]:


# Bandas necesarias para el cálculo
b_red = rioxarray.open_rasterio(assets["B04"].href)
b_nir = rioxarray.open_rasterio(assets["B8A"].href)


# Para efectos del ejemplo, se reduce el área en la que va a realizarse el cálculo.

# In[ ]:


# Buffer (rectángulo) de 15 km alrededor de un punto
point = Point(859872, 1168852)
bbox = point.buffer(15000).bounds

# Recorte 
b_red_clip = b_red.rio.clip_box(*bbox)
b_nir_clip = b_nir.rio.clip_box(*bbox)


# In[ ]:


# Visualización de la banda roja
b_red_clip.plot(robust=True, cmap="Reds")


# In[ ]:


# Visualización de la banda infrarroja cercana
b_nir_clip.plot(robust=True, cmap="Reds")


# In[ ]:


# Dimensiones de las bandas
print(b_red_clip.shape, b_nir_clip.shape)


# Para realizar la operación algebraica, las bandas deben tener las mismas dimensiones. Así que se reduce la resolución de la banda roja para hacerla igual a la resolución de la infrarroja cercana.

# In[ ]:


# Se homogeneizan las dimensiones
b_red_clip_matched = b_red_clip.rio.reproject_match(b_nir_clip)
print(b_red_clip_matched.shape)


# Ya puede calcularse el NDVI.

# In[ ]:


# Cálculo del NDVI
ndvi = (b_nir_clip - b_red_clip_matched)/ (b_nir_clip + b_red_clip_matched)


# In[ ]:


# Visualización del cálculo del NDVI
ndvi.plot(robust=True)


# ## Escritura

# La función [to_raster()](https://corteva.github.io/rioxarray/html/rioxarray.html#rioxarray.raster_array.RasterArray.to_raster) exporta los datos a un archivo raster.

# In[ ]:


# Se guarda el resultado del cálculo del NDVI en un archivo
# ndvi.rio.to_raster("ndvi.tif")


# ## Recursos de interés

# - [The Carpentries Incubator - Introduction to Geospatial Raster and Vector Data with Python](https://carpentries-incubator.github.io/geospatial-python/)
# - [Geospatial Raster & Vector Data with Python](https://www.youtube.com/watch?v=Ce7GuGIf3r0)

# In[ ]:




