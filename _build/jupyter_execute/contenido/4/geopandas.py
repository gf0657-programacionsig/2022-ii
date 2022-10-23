#!/usr/bin/env python
# coding: utf-8

# # pandas: paquete para análisis y manipulación de datos

# ## Descripción general

# [pandas](https://pandas.pydata.org/) es una biblioteca de Python para análisis y manipulación de datos. Proporciona estructuras de datos y operaciones para manejar tablas numéricas y series temporales. Fue creada por Wes McKinney in 2008. El nombre "pandas" hace referencia tanto a "*Panel Data*" como a "*Python Data Analysis*".
# 
# Como su estructura principal, pandas implementa el `DataFrame`, el cual es un arreglo rectangular de datos, organizado en filas y columnas.

# ## Carga

# In[1]:


# Se acostumbra cargar pandas con el alias pd

import pandas as pd


# ## Estructuras de datos
# Las dos principales estructuras de datos de pandas son `Series` y `DataFrames`.

# ### Series
# Las [Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html?highlight=series#pandas.Series) son arreglos unidimensionales que contienen datos de cualquier tipo. Se asemejan a una columna de una tabla.

# In[2]:


# Definición de una serie

primos = [2, 3, 5, 7, 11]
serie_primos = pd.Series(primos)

serie_primos


# Cada elemento de una serie tiene un índice (i.e. posición), comenzando con 0.

# In[3]:


# Primer elemento
print("Primer elemento:", serie_primos[0])

# Segundo elemento
print("Segundo elemento:", serie_primos[1])


# Los índices también pueden tener etiquetas personalizadas.

# In[4]:


# Índice de una serie con etiquetas personalizadas

serie_primos = pd.Series(primos, index = ["A", "B", "C", "D", "E"])

serie_primos


# In[5]:


# Elemento en el índice "D"
print(serie_primos["D"])


# ### DataFrames
# Los [DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame) son estructuras multidimensionales. Una serie puede verse como una columna de una tabla y un dataframe como una tabla completa. Un dataframe puede construirse a partir de varias series.

# In[6]:


# Dataframe construído a partir de dos series

datos = {
  "pais": ["PA", "CR", "NI"],
  "poblacion": [4.1, 5.0, 6.6]
}

paises = pd.DataFrame(datos)

paises


# El operador **loc** permite retornar una o más filas de un dataframe, de acuerdo con un índice o con un vector de índices.

# In[7]:


# Segundo elemento
paises.loc[1]


# In[8]:


# Segundo y tercer elemento
paises.loc[[1, 2]]


# Los índices de los dataframes también pueden etiquetarse:

# In[9]:


paises = pd.DataFrame(datos, index=["pais0", "pais1", "pais2"])
paises


# In[10]:


# Elemento en "pais0"
paises.loc["pais0"]


# ## Operaciones básicas

# Seguidamente, se describen y ejemplifican algunas de las funciones básicas de pandas.
# 
# En los siguientes ejemplos, se utilizará un conjunto de registros de presencia de felinos (familia *Felidae*) de Costa Rica, obtenido a través de una [consulta al portal de GBIF](https://www.gbif.org/occurrence/download/0016217-210914110416597).

# ### read_csv() - carga de datos

# In[11]:


felinos = pd.read_csv("https://raw.githubusercontent.com/gf0657-programacionsig/2022-ii/main/contenido/3/datos/gbif/felinos.csv", sep="\t")


# ### info() - información general sobre un conjunto de datos

# In[12]:


felinos.info()


# ### head(), tail(), sample() - despliegue de filas de un conjunto de datos

# In[13]:


# Primeros 10 registros
felinos.head()


# In[14]:


# Últimos 15 registros
felinos.tail()


# In[15]:


# 5 registros seleccionados aleatoriamente
felinos.sample(5)


# Los contenidos de un data frame también pueden desplegarse al escribir su nombre en la consola de Python.

# In[16]:


felinos


# ### Selección de columnas

# Las columnas que se despliegan en un data frame pueden especificarse mediante una lista.

# In[17]:


# Despliegue de las columnas con el nombre científico, la especie, la fecha, el año, el mes y el día

felinos[["scientificName", "species", "eventDate", "year", "month", "day"]]


# ### Selección de filas

# In[18]:


# Selección de filas correspondientes a jaguares (*Panthera onca*)
jaguares = felinos[felinos["species"] == "Panthera onca"]

# Despliegue de los primeros registros
jaguares.head()


# In[19]:


# Selección de filas correspondientes a jaguares (*Panthera onca*) o pumas (*Puma concolor*)
jaguares_pumas = felinos[(felinos["species"] == "Panthera onca") | (felinos["species"] == "Puma concolor")]

# Despliegue de los primeros registros
jaguares_pumas.head(10)


# ## Operaciones de análisis

# ### Graficación

# #### Carga de bibliotecas

# In[20]:


import matplotlib.pyplot as plt # biblioteca de graficación
get_ipython().run_line_magic('matplotlib', 'inline')

import calendar # biblioteca para manejo de fechas


# #### Estilo de los gráficos

# In[21]:


# Estilo de los gráficos
plt.style.use('ggplot')


# #### Ejemplos de gráficos

# ##### Distribución de registros de presencia por año

# In[22]:


# Cambio del tipo de datos del campo de fecha
felinos["eventDate"] = pd.to_datetime(felinos["eventDate"])

# Agrupación de los registros por año
felinos_registros_x_anio = felinos.groupby(felinos['eventDate'].dt.year).count().eventDate

felinos_registros_x_anio


# In[23]:


# Tipo de datos retornado
type(felinos_registros_x_anio)


# In[24]:


# Conversión de series a dataframe
felinos_registros_x_anio_df = pd.DataFrame({'anio':felinos_registros_x_anio.index, 'registros':felinos_registros_x_anio.values}) 

# Conversión del tipo de la columna de año
felinos_registros_x_anio_df["anio"] = pd.to_numeric(felinos_registros_x_anio_df["anio"], downcast='integer')
felinos_registros_x_anio_df.style.set_precision(2)

felinos_registros_x_anio_df


# In[25]:


# Graficación
felinos_registros_x_anio_df.plot(x='anio', y='registros', kind='bar', figsize=(12,7), color='red')

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por año', fontsize=20)
plt.xlabel('Año', fontsize=16)
plt.ylabel('Cantidad de registros', fontsize=16)


# ##### Distribución de registros de presencia por mes

# In[26]:


# Agrupación de los registros por mes
felinos_registros_x_mes = felinos.groupby(felinos['eventDate'].dt.month).count().eventDate

felinos_registros_x_mes


# In[27]:


# Reemplazo del número del mes por el nombre del mes
felinos_registros_x_mes.index=[calendar.month_name[x] for x in range(1,13)]

felinos_registros_x_mes


# In[28]:


# Gráfico de barras
felinos_registros_x_mes.plot(kind='bar',figsize=(12,7), color='blue', alpha=0.5)

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por mes', fontsize=20)
plt.xlabel('Mes', fontsize=16)
plt.ylabel('Cantidad de registros', fontsize=16);


# ##### Graficación en una línea de tiempo

# In[29]:


# Agrupación de los registros por fecha
registros_x_fecha = felinos.groupby(felinos['eventDate'].dt.date).count().eventDate

registros_x_fecha


# In[30]:


# Gráfico de líneas
registros_x_fecha.plot(figsize=(20,8), color='blue')

# Título y leyendas en los ejes
plt.title('Registros de presencia de Felidae (felinos) en Costa Rica por fecha', fontsize=20)
plt.xlabel('Fecha',fontsize=16)
plt.ylabel('Cantidad de registros',fontsize=16);
plt.legend()

