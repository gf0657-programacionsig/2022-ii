#!/usr/bin/env python
# coding: utf-8

# # Manejo de datos raster

# ## Descripción general

# En este capítulo, se muestran ejemplos de manejo de datos raster con Python.
# 
# Los datos se obtienen de servicios basados en [SpatioTemporal Asset Catalogs (STAC)](https://stacspec.org). STAC es una especificación que proporciona una estructura común para describir y catalogar recursos espacio temporales (ej. imágenes satelitales). Puede explorar catálogos STAC con [STAC browser](https://radiantearth.github.io/stac-browser/).
# 
# Algunas de los módulos que se utilizan en este capítulo son:
# 
# - [rasterio](https://rasterio.readthedocs.io/): para operaciones generales de manejo de datos raster.
# - [pystac_client](https://pystac-client.readthedocs.io/): para trabajar con catálogos STAC.
# - [rioxarray](https://corteva.github.io/rioxarray/stable/): extensión de [xarray](https://docs.xarray.dev/en/stable/) para trabajar con rasterio. 

# ## Instalación de módulos

# ```
# mamba install -c conda-forge xarray rioxarray earthpy xarray-spatial pystac-client python-graphviz
# ```

# ## Acceso a datos raster

# In[1]:


# Carga de pystac_client
from pystac_client import Client


# In[2]:


# URL de un catálogo STAC
api_url = "https://earth-search.aws.element84.com/v0"

client = Client.open(api_url)


# In[3]:


# Colección
collection = "sentinel-s2-l2a-cogs"  # Sentinel-2, Nivel 2A, COG


# In[4]:


# Punto para búsqueda
from shapely.geometry import Point
point = Point(-84, 10)


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


# In[9]:


# Primer item (imagen) retornado
item = items[0]


# In[10]:


# Algunos atributos del item
print(item.datetime)
print(item.geometry)
print(item.properties)


# In[11]:


# Rectángulo para búsquedas
bbox = point.buffer(0.01).bounds
bbox


# In[12]:


# Búsqueda con nuevos criterios
search = client.search(collections=[collection],
                       bbox=bbox,
                       datetime="2022-01-01/2022-11-30",
                       query=["eo:cloud_cover<10"]) # no deben haber espacios alrededor del '<'

# Cantidad total de items que retorna la búsqueda
search.matched()


# In[13]:


# Items retornados
items = search.get_all_items()

len(items)


# In[14]:


# Segundo item y algunos de sus atributos
item = items[1]

print(item.datetime)
print(item.properties)


# In[15]:


# Activos (assets) del item
assets = item.assets

# Llaves
assets.keys()


# In[16]:


assets.items()


# In[17]:


# Nombres de los activos
for key, asset in assets.items():
    print(f"{key}: {asset.title}")


# In[18]:


# Imagen thumbnail
assets["thumbnail"]


# In[19]:


# Dirección del thumbnail
assets["thumbnail"].href


# In[20]:


import rioxarray


# In[21]:


# Dirección de la banda 9
b09_href = assets["B09"].href
b09_href


# In[22]:


# Banda 9
b09 = rioxarray.open_rasterio(b09_href)
b09


# In[23]:


b09.values


# In[24]:


# Graficación de la banda
b09.plot(robust=True)


# In[25]:


# Vista general de la imagen (True Color)
overview = rioxarray.open_rasterio(item.assets['overview'].href)
overview


# In[26]:


overview.shape


# In[27]:


overview.plot.imshow(figsize=(8, 8))


# ## Cálculo del NDVI

# In[28]:


# Bandas necesarias para el cálculos
b_red = rioxarray.open_rasterio(assets["B04"].href)
b_nir = rioxarray.open_rasterio(assets["B8A"].href)


# In[29]:


# Se reduce el área de cálculo
point = Point(859872, 1168852)
bbox = point.buffer(15000).bounds

b_red_clip = b_red.rio.clip_box(*bbox)
b_nir_clip = b_nir.rio.clip_box(*bbox)


# In[30]:


b_red_clip.plot(robust=True)


# In[31]:


b_nir_clip.plot(robust=True)


# In[32]:


# Dimensiones de las bandas
print(b_red_clip.shape, b_nir_clip.shape)


# In[33]:


# Se homogenizan las dimensiones
b_red_clip_matched = b_red_clip.rio.reproject_match(b_nir_clip)
print(b_red_clip_matched.shape)


# In[34]:


# Cálculo del NDVI
ndvi = (b_nir_clip - b_red_clip_matched)/ (b_nir_clip + b_red_clip_matched)
print(ndvi)


# In[35]:


ndvi.plot(robust=True)


# In[36]:


# Se guarda el resultado en un archivo
# ndvi.rio.to_raster("ndvi.tif")


# ## Recursos de interés

# - [The Carpentries Incubator - Introduction to Geospatial Raster and Vector Data with Python](https://carpentries-incubator.github.io/geospatial-python/)
# - [Geospatial Raster & Vector Data with Python](https://www.youtube.com/watch?v=Ce7GuGIf3r0)

# In[ ]:




