#!/usr/bin/env python
# coding: utf-8

# # Ejercicios

# In[1]:


import pandas as pd
import geopandas as gpd


# ## Datos

# ### Provincias

# In[2]:


provincias = gpd.read_file("datos/ign/provincias.geojson")

provincias.plot()


# ### Cantones

# In[3]:


cantones = gpd.read_file("datos/ign/cantones.geojson")

cantones.plot()


# ### COVID

# In[4]:


# Carga de casos positivos en cantones
covid_cantonal_positivos = pd.read_csv("datos/ministerio-salud/05_30_22_CSV_POSITIVOS.csv", 
                                       sep=";", 
                                       encoding="iso-8859-1") # para leer tildes y otros caracteres
# Reducción de columnas
covid_cantonal_positivos = covid_cantonal_positivos[["cod_provin", "cod_canton", "provincia", "canton", "30/05/2022"]]

# Eliminación de fila con valores nulos
covid_cantonal_positivos = covid_cantonal_positivos.dropna(how='all')

# Eliminación de fila con canton=="Otros"
covid_cantonal_positivos = covid_cantonal_positivos[covid_cantonal_positivos["canton"] != "Otros"]

# Cambio de nombre de columnas
covid_cantonal_positivos = covid_cantonal_positivos.rename(columns={"30/05/2022": "positivos"})


covid_cantonal_positivos


# In[5]:


# Casos positivos en provincias
covid_provincial_positivos = covid_cantonal_positivos.groupby("cod_provin")["positivos"].sum()

covid_provincial_positivos


# ## Merge de cantones y COVID

# In[6]:


cantones_covid = cantones.merge(covid_cantonal_positivos, on='cod_canton')

cantones_covid


# In[7]:


cantones_covid.plot(column = "positivos", 
                    legend=True,
                    cmap='OrRd', 
                    scheme='quantiles',
                    figsize=(20, 20)
                    )


# ## Merge de provincias y COVID

# In[8]:


provincias_covid = provincias.merge(covid_provincial_positivos, on='cod_provin')

provincias_covid


# In[9]:


provincias_covid.plot(column = "positivos", 
                    legend=True,
                    cmap='OrRd', 
                    scheme='quantiles',
                    figsize=(20, 20)
                    )


# In[ ]:




