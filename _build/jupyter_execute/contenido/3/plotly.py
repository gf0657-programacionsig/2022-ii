#!/usr/bin/env python
# coding: utf-8

# # Visualización de datos con plotly

# **NOTA IMPORTANTE**
# 
# Por una falla de Jupyter Book (la biblioteca usada para construir el sitio web de este curso), los gráficos en Plotly no se están desplegando, pero pueden verse en el sitio:
# 
# [https://nbviewer.org/github/gf0657-programacionsig/2022-ii/blob/main/contenido/3/plotly.ipynb](https://nbviewer.org/github/gf0657-programacionsig/2022-ii/blob/main/contenido/3/plotly.ipynb)

# ## Descripción general

# [Plotly Python](https://plotly.com/python/) es una biblioteca para gráficos interactivos que forma parte del [grupo de bibliotecas de graficación de Plotly](https://plotly.com/graphing-libraries/), el cual también incluye bibliotecas para otros lenguajes como R, Julia, F# y MATLAB. Plotly fue originalmente escrita en [JavaScript](https://en.wikipedia.org/wiki/JavaScript), por lo que es particularmente adecuada para gráficos interactivos en la Web.
# 
# El módulo [plotly.express](https://plotly.com/python/plotly-express/) provee [más de 30 funciones para crear diferentes tipos de gráficos](https://plotly.com/python-api-reference/plotly.express.html) y se recomienda como punto de partida para programar los tipos de gráficos estadísticos más comunes.

# ## Instalación de la biblioteca

# Puede instalarse con `pip`, `conda` o `mamba`, desde la línea de comandos del sistema operativo, con alguna de las siguientes opciones:

# ```
# # Con pip:
# pip install plotly
# 
# # Con conda:
# conda install plotly -c conda-forge
# 
# # Con mamba:
# mamba install plotly -c conda-forge
# ```

# ## Carga de la bibliotecas

# In[1]:


# Carga de plotly express
import plotly.express as px

# Carga de plotly figure factory,
# para tipos adicionales de gráficos
import plotly.figure_factory as ff

# Carga de pandas
import pandas as pd


# ## Conjuntos de datos para pruebas

# ### Casos de COVID-19 en Costa Rica

# Estos datos son publicados por el Ministerio de Salud de Costa Rica en [https://geovision.uned.ac.cr/oges/](https://geovision.uned.ac.cr/oges/). Se distribuyen en archivos CSV, incluyendo un archivo de datos generales para todo el país y varios archivos con datos por cantón. La fecha de la última actualización es 2022-05-30.

# #### Datos generales

# ##### Carga de datos

# Es un archivo que contiene una fila por día y varias columnas con cantidades de casos (positivos, fallecidos, en salón, en UCI, etc.)

# In[2]:


# Carga de datos generales
covid_general = pd.read_csv("datos/ministerio-salud/covid/05_30_22_CSV_GENERAL.csv", sep=";")


# Estructura del conjunto de datos.

# In[3]:


# Estructura del conjunto de datos
covid_general.info()


# Visualización de los datos.

# In[4]:


# Datos generales
covid_general


# Puede notarse una cantidad muy grande de columnas (no todas son necesarias) y que la columna correspondiente a la fecha es una hilera de caracteres y no de tipo `Date`. También que hay algunos nombres de columnas en mayúsculas y otros en minúsculas.

# ##### Reducción, cambio de nombre y cambio de tipo de datos de columnas

# In[5]:


# Reducción de columnas
covid_general = covid_general[["FECHA", "positivos", "activos", "RECUPERADOS", "fallecidos", 
                               "nue_posi", "nue_falleci", "salon", "UCI"]]

# Cambio de nombre de las columnas a minúsculas y a nombres más claros
covid_general = covid_general.rename(columns={"FECHA": "fecha",
                                              "RECUPERADOS": "recuperados",
                                              "nue_posi": "nuevos_positivos",
                                              "nue_falleci": "nuevos_fallecidos",
                                              "UCI": "uci"})

# Cambio del tipo de datos del campo de fecha
covid_general["fecha"] = pd.to_datetime(covid_general["fecha"], format="%d/%m/%Y")


# In[6]:


# Despliegue de los cambios
covid_general


# #### Datos cantonales

# Son cuatro archivos con casos positivos, activos, recuperados y fallecidos. Cada archivo tiene una fila para cada uno de los 82 cantones y una fila adicional para "Otros". Hay una columna por cada día muestreado, con la cantidad de casos del tipo respectivo.

# ##### Carga de datos

# In[7]:


# Carga de casos positivos
covid_cantonal_positivos = pd.read_csv("datos/ministerio-salud/covid/05_30_22_CSV_POSITIVOS.csv", 
                                       sep=";", 
                                       encoding="iso-8859-1") # para leer tildes y otros caracteres

# Carga de casos activos
covid_cantonal_activos = pd.read_csv("datos/ministerio-salud/covid/05_30_22_CSV_ACTIVOS.csv", 
                                     sep=";", 
                                     encoding="iso-8859-1") # para leer tildes y otros caracteres

# Carga de casos recuperados
covid_cantonal_recuperados = pd.read_csv("datos/ministerio-salud/covid/05_30_22_CSV_RECUP.csv", 
                                         sep=";", 
                                         encoding="iso-8859-1") # para leer tildes y otros caracteres

# Carga de casos fallecidos
covid_cantonal_fallecidos = pd.read_csv("datos/ministerio-salud/covid/05_30_22_CSV_FALLECIDOS.csv", 
                                        sep=";", 
                                        encoding="iso-8859-1") # para leer tildes y otros caracteres


# Estructura de los conjuntos de datos.

# In[8]:


# Estructura de los conjuntos de datos.
covid_cantonal_positivos.info()


# Visualización inicial de los datos.

# In[9]:


# Casos positivos
covid_cantonal_positivos


# Puede notarse una cantidad muy grande de columnas y también la presencia de caracteres especiales (/) en muchos de los nombres de estas. También que hay una fila con un cantón correspondiente a "Otros" y otra con valores nulos.

# ##### Reducción y cambio de nombre de columnas y eliminación de filas innecesarias

# Se reduce la cantidad de columnas, de manera que solo se conservan las que corresponde a la última fecha muestreada, al nombre del cantón y al de la provincia. También se eliminan las filas con valores nulos u "Otros".

# In[10]:


# Reducción de columnas
covid_cantonal_positivos = covid_cantonal_positivos[["provincia", "canton", "30/05/2022"]]
covid_cantonal_fallecidos = covid_cantonal_fallecidos[["provincia", "canton", "30/05/2022"]]
covid_cantonal_recuperados = covid_cantonal_recuperados[["provincia", "canton", "30/05/2022"]]
covid_cantonal_activos = covid_cantonal_activos[["provincia", "canton", "30/05/2022"]]

# Eliminación de fila con valores nulos
covid_cantonal_positivos = covid_cantonal_positivos.dropna(how='all')
covid_cantonal_fallecidos = covid_cantonal_fallecidos.dropna(how='all')
covid_cantonal_recuperados = covid_cantonal_recuperados.dropna(how='all')
covid_cantonal_activos = covid_cantonal_activos.dropna(how='all')

# Eliminación de fila con canton=="Otros"
covid_cantonal_positivos = covid_cantonal_positivos[covid_cantonal_positivos["canton"] != "Otros"]
covid_cantonal_fallecidos = covid_cantonal_fallecidos[covid_cantonal_fallecidos["canton"] != "Otros"]
covid_cantonal_recuperados = covid_cantonal_recuperados[covid_cantonal_recuperados["canton"] != "Otros"]
covid_cantonal_activos = covid_cantonal_activos[covid_cantonal_activos["canton"] != "Otros"]

# Cambio de nombre de columnas
covid_cantonal_positivos = covid_cantonal_positivos.rename(columns={"30/05/2022": "positivos"})
covid_cantonal_fallecidos = covid_cantonal_fallecidos.rename(columns={"30/05/2022": "fallecidos"})
covid_cantonal_recuperados = covid_cantonal_recuperados.rename(columns={"30/05/2022": "recuperados"})
covid_cantonal_activos = covid_cantonal_activos.rename(columns={"30/05/2022": "activos"})


# In[11]:


# Despliegue de los cambios
covid_cantonal_positivos


# ### Pasajeros del Titanic

# Este es el conjunto de datos de entrenamiento de la competencia [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview) organizada por [Kaggle](https://www.kaggle.com/). El archivo también está disponible en [https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii/blob/main/contenido/b/datos/entrenamiento.csv](https://github.com/pf3311-cienciadatosgeoespaciales/2021-iii/blob/main/contenido/b/datos/entrenamiento.csv).

# #### Carga de datos

# In[12]:


# Pasajeros en el conjunto de datos de entrenamiento
titanic = pd.read_csv("datos/kaggle/titanic/pasajeros-titanic-entrenamiento.csv")

# Despliegue de los datos
titanic


# ## Visualizaciones de datos

# Las siguientes visualizaciones se implementan con los métodos de plotly.express (px).

# ### Histogramas

# Un [histograma](https://es.wikipedia.org/wiki/Histograma) es una representación gráfica de la distribución de una variable numérica en forma de barras (llamadas en inglés *bins*). La longitud de cada barra representa la frecuencia de un rango de valores de la variable. La graficación de la distribución de las variables es, frecuentemente, una de las primeras tareas que se realiza cuando se explora un conjunto de datos.
# 
# En plotly.express, los histogramas se crean con el método [plotly.express.histogram()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.histogram.html). Se recomienda revisar también el [tutorial](https://plotly.com/python/histograms/).

# El siguiente histograma muestra la distribución de la variable correspondiente a los casos de COVID positivos en los cantones de Costa Rica.

# In[13]:


# Histograma de casos positivos en cantones
px.histogram(covid_cantonal_positivos, 
             x="positivos", # variable a graficar
             nbins=8, # cantidad de bins
             title="Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30",
             labels={"positivos": "Casos"})


# El argumento `color` permite colorear el histograma por una variable adicional.

# In[14]:


# Histograma de casos positivos en cantones coloreado por provincia
px.histogram(covid_cantonal_positivos, 
             x="positivos", 
             nbins=8,
             color="provincia", # variable a colorear
             title="Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30",
             labels={"positivos": "Casos", "provincia": "Provincia"})


# Un gráfico marginal permite ver detalles adicionales de los datos que no muestra el histograma.

# In[15]:


# Histograma de casos positivos con gráfico marginal
px.histogram(covid_cantonal_positivos, 
             x="positivos", 
             nbins=8,
             marginal="rug", # gráfico en el margen: 'rug', 'box', 'violin', o 'histogram'
             color="provincia",
             title="Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30",
             labels={"positivos": "Casos", "provincia": "Provincia"})


# Los *facets* permiten generar subgráficos con base en una variable y así comparar los datos para cada valor de la variable.

# In[16]:


# Facets por provincia
px.histogram(covid_cantonal_positivos, 
             x="positivos", 
             nbins=8,
             marginal="rug",
             color="provincia",
             facet_col="provincia", # se generan facets por provincia
             labels={"positivos": "Casos", "provincia": "Pr"})


# El método [plotly.figure_factory.create_distplot()](https://plotly.github.io/plotly.py-docs/generated/plotly.figure_factory.create_distplot.html) crea un histograma y una estimación de densidad del kernel (*Kernel Density Estimation*, KDE), una curva que muestra la densidad de los datos. Se recomienda revisar el [tutorial](https://plotly.com/python/distplot/).

# In[17]:


# Histograma y curva de densidad

# Lista de valores a graficar
positivos = covid_cantonal_positivos["positivos"].values.tolist()
datos = [positivos]

# Etiquetas para la leyenda
etiquetas = ['positivos']

# Se crea la figura
fig = ff.create_distplot(datos, etiquetas, show_hist=False)

# Se muestra la figura
fig.show()


# #### Ejercicios

# 1. Construya un histograma que muestre la distribución de la edad de los pasajeros del Titanic. Incluya una curva de densidad.
# 2. Agregue la distribución de la variable de sobrevivencia al histograma del ejercicio anterior.
# 
# 3. Construya un histograma que muestre la distribución de la cantidad de padres e hijos que viajaban con los pasajeros del Titanic. Incluya una curva de densidad.
# 4. Agregue la distribución de la variable de sobrevivencia al histograma del ejercicio anterior.
# 
# 5. Construya un histograma que muestre la distribución de la cantidad de hermanos y cónyugues que viajaban con los pasajeros del Titanic. Incluya una curva de densidad.
# 6. Agregue la distribución de la variable de sobrevivencia al histograma del ejercicio anterior.

# ### Gráficos de caja

# Un [gráfico de caja (*boxplot*)](https://es.wikipedia.org/wiki/Diagrama_de_caja) muestra información de una variable numérica a través de su [mediana](https://es.wikipedia.org/wiki/Mediana), sus [cuartiles](https://es.wikipedia.org/wiki/Cuartiles) (Q1, Q2 y Q3) y sus [valores atípicos](https://es.wikipedia.org/wiki/Valor_at%C3%ADpico).
# 
# En plotly.express, los gráficos de caja se crean con el método [plotly.express.box()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.box.html). Se recomienda revisar el [tutorial](https://plotly.com/python/box-plots/).

# El siguiente diagrama de caja muestra la distribución de la variable correspondiente a los casos de COVID fallecidos en los cantones de Costa Rica.

# In[18]:


# Gráfico de caja de casos fallecidos en cantones
px.box(covid_cantonal_fallecidos,
       y="fallecidos",
       hover_data=["canton"], # campo que se despliega con el ratón
       title="Distribución de la cantidad de casos fallecidos de COVID en cantones de Costa Rica al 2022-05-30",
       labels={"fallecidos":"Casos", "canton":"Cantón"})


# In[19]:


# Gráfico de caja de casos fallecidos en cantones, agrupados por provincia
px.box(covid_cantonal_fallecidos,
       y="fallecidos",
       x="provincia",
       hover_data=["canton"], # campo que se despliega con el ratón
       title="Distribución de la cantidad de casos fallecidos de COVID en cantones de Costa Rica al 2022-05-30",
       labels={"fallecidos":"Casos", "provincia": "Provincia", "canton":"Cantón"})


# In[20]:


# Gráfico de caja de casos fallecidos en cantones, agrupados por provincia
# y con despliegue de puntos de datos de cantones
px.box(covid_cantonal_fallecidos,
       y="fallecidos",
       x="provincia",
       hover_data=["canton"], # campo que se despliega con el ratón
       points="all", # puntos de datos: 'outliers', 'suspectedoutliers', 'all'
       title="Distribución de la cantidad de casos fallecidos de COVID en cantones de Costa Rica al 2022-05-30",
       labels={"fallecidos":"Casos", "provincia": "Provincia", "canton":"Cantón"})


# #### Ejercicios

# 1. Construya un gráfico de caja de la edad de los pasajeros del Titanic.
# 2. Agregue la distribución de la variable de sobrevivencia al gráfico del ejercicio anterior.
# 
# 3. Construya un gráfico de caja de la cantidad de padres e hijos que viajaban con los pasajeros del Titanic.
# 4. Agregue la distribución de la variable de sobrevivencia al gráfico del ejercicio anterior.
# 
# 5. Construya un gráfico de caja de la cantidad de hermanos y cónyugues que viajaban con los pasajeros del Titanic.
# 6. Agregue la distribución de la variable de sobrevivencia al gráfico del ejercicio anterior.

# ### Gráficos de *strip*

# El método [plotly.express.strip()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.strip.html) implementa un gráfico de "franja" (*strip*) o de "oscilación" (*jittered*). Se recomienda revisar el [tutorial](https://plotly.com/python/strip-charts/).

# In[21]:


# Gráfico de casos positivos en cantones
px.strip(covid_cantonal_positivos, 
         x="positivos", 
         hover_name="canton",
         title="Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30",
         labels={"positivos": "Casos"})


# In[22]:


# Gráfico de casos positivos en cantones coloreado por provincia
px.strip(covid_cantonal_positivos, 
         x="positivos", 
         hover_name="canton", 
         color="provincia",
         title="Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30",
         labels={"positivos": "Casos", "provincia": "Provincia"})


# In[23]:


# Gráfico de casos positivos en cantones coloreado y dividido por provincia
px.strip(covid_cantonal_positivos, 
         y="positivos", # se usa el eje y para la orientación vertical
         orientation="v", # orientación vertical
         hover_name="canton", 
         color="provincia",
         facet_col="provincia",
         title="Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30",
         labels={"positivos": "Casos", "provincia": "Pr"})


# ### Gráficos de barras

# Un [gráfico de barras](https://es.wikipedia.org/wiki/Diagrama_de_barras) se compone de barras rectangulares con longitud proporcional a estadísticas (ej. frecuencias, promedios, mínimos, máximos) asociadas a una variable categórica o discreta. Las barras pueden ser horizontales o verticales y se recomienda que estén ordenadas según su longitud, a menos que exista un orden inherente a la variable (ej. el orden de los días de la semana o de los meses del año).

# En plotly.express, los gráficos de barras se crean con el método [plotly.express.bar()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.bar.html). Se recomienda revisar el [tutorial](https://plotly.com/python/bar-charts/).

# El siguiente gráfico de barras verticales muestra las cantidades de casos positivos en los cantones de Limón.

# In[24]:


# Subconjunto de cantones de la provincia de Limón
covid_limon_positivos = covid_cantonal_positivos[covid_cantonal_positivos["provincia"] == "Limón"]

# Se establece la columna "canton" como índice del dataframe
# y este se ordena por la cantidad de casos positivos
covid_limon_positivos = covid_limon_positivos.set_index("canton") \
                                             .sort_values(by="positivos", ascending=False)

px.bar(covid_limon_positivos, 
       y="positivos", 
       orientation="v",
       title="Cantidad de casos positivos de COVID en los cantones de Limón al 2022-05-30",
       labels={"positivos":"Casos", "canton":"Cantón"})


# El siguiente gráfico de barras horizontales muestra las cantidades de casos activos en los cantones de San José.

# In[25]:


# Subconjunto de cantones de la provincia de San José
covid_sanjose_activos = covid_cantonal_activos[covid_cantonal_activos["provincia"] == "San José"]

# Se establece la columna "canton" como índice del dataframe
# y este se ordena por la cantidad de casos positivos
covid_sanjose_activos = covid_sanjose_activos.set_index("canton") \
                                             .sort_values(by="activos")

px.bar(covid_sanjose_activos, 
       x="activos", 
       orientation="h",
       height=800, # altura del gráfico
       title="Cantidad de casos activos de COVID en los cantones de San José al 2022-05-30",
       labels={"activos":"Casos", "canton":"Cantón"})


# En el siguiente ejemplo, se utiliza el método [pandas.DataFrame.groupby()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) para agrupar los datos por provincia y sumar los casos positivos.

# In[26]:


# Suma de casos positivos por provincia
covid_provincial_positivos = covid_cantonal_positivos.groupby(["provincia"], as_index=False)["positivos"] \
                                                     .sum()

# Se establece la columna "provincia" como índice del dataframe
# y este se ordena por la cantidad de casos positivos
covid_provincial_positivos = covid_provincial_positivos.set_index("provincia") \
                                                       .sort_values(by="positivos", ascending=False)

px.bar(covid_provincial_positivos, 
       y="positivos",
       title="Cantidad de casos positivos de COVID en las provincias de Costa Rica al 2022-05-30",
       labels={"positivos":"Casos", "provincia":"Provincia"})


# El siguiente gráfico muestra la cantidad de pasajeros del Titanic distribuidos por sexo y sobrevivencia.

# In[27]:


# Gráfico de barras

# Columna con valores "Sobreviviente" y "Fallecido"
titanic['Survived_text'] = ["Survived" if x ==1 else "Dead" for x in titanic['Survived']]

px.bar(titanic, 
       x="Sex", 
       color="Survived_text",
       color_discrete_sequence=["red", "blue"], # lista de colores
       title="Cantidad de pasajeros sobrevivientes y fallecidos del Titanic distribuidos por sexo",
       labels={"Sex":"Sexo", "Survived_text":"Sobrevivencia"})


# ### Gráficos de pastel

# Un [gráfico de pastel](https://es.wikipedia.org/wiki/Gr%C3%A1fico_circular) representa porcentajes y porciones en secciones (*slices*) de un círculo. Son muy populares, pero también criticados debido a la dificultad del cerebro humano de comparar áreas de sectores circulares, por lo que algunos expertos recomiendan sustituirlos por otros tipos de gráficos como, por ejemplo, gráficos de barras.

# En plotly.express, los gráficos de barras se crean con el método [plotly.express.pie()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.pie.html). Se recomienda revisar el [tutorial](https://plotly.com/python/pie-charts/).

# El siguiente gráfico de barras verticales muestra las cantidades de casos positivos en los cantones de Limón.

# In[28]:


# Subconjunto de cantones de la provincia de Limón
covid_limon_positivos = covid_cantonal_positivos[covid_cantonal_positivos["provincia"] == "Limón"]

# Se establece la columna "canton" como índice del dataframe
# y este se ordena por la cantidad de casos positivos
covid_limon_positivos = covid_limon_positivos.sort_values(by="positivos", ascending=False)

px.pie(covid_limon_positivos, 
       names="canton", 
       values='positivos',
       color_discrete_sequence=px.colors.sequential.YlOrRd[::-1],
       title="Porcentaje de casos positivos de COVID en los cantones de Limón al 2022-05-30",
       labels={"canton":"Cantón", "positivos":"Casos"})


# In[29]:


# Suma de casos positivos por provincia
covid_provincial_positivos = covid_cantonal_positivos.groupby(["provincia"], as_index=False)["positivos"] \
                                                     .sum()

# Se establece la columna "provincia" como índice del dataframe
# y este se ordena por la cantidad de casos positivos
covid_provincial_positivos = covid_provincial_positivos.sort_values(by="positivos", ascending=False)

px.pie(covid_provincial_positivos, 
       names="provincia",
       values="positivos",
       title="Cantidad de casos positivos de COVID en las provincias de Costa Rica al 2022-05-30",
       labels={"positivos":"Casos", "provincia":"Provincia"})


# #### Ejercicios

# 1. Construya un gráfico de pastel que muestre la proporción de pasajeros sobrevivientes y fallecidos que viajaban en el Titanic.
# 2. Construya un gráfico de pastel que muestre la proporción de cada sexo (masculino, femenino) de pasajeros que viajaban en el Titanic.
# 3. Construya un gráfico de pastel que muestre la proporción de cada clase de pasajeros (1, 2, 3) que viajaban en el Titanic.

# ### *Treemaps*

# Los [*treemaps*](https://en.wikipedia.org/wiki/Treemapping) se utilizan para mostrar datos organizados de manera jerárquica, usualmente en rectángulos.
# 
# En plotly.express, los *treemaps* se implementan con el método [plotly.express.treemap()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.treemap.html). Se recomienda revisar el [tutorial](https://plotly.com/python/treemaps/).

# In[30]:


# Treemap de casos positivos en cantones (una variable)
px.treemap(covid_cantonal_positivos, 
           values="positivos",
           color_discrete_sequence=px.colors.sequential.YlOrRd[::-1],
           path=["canton"], # jerarquía de variables
           title="Casos positivos de COVID en los cantones de Costa Rica al 2022-05-30")


# In[31]:


# Treemap de casos positivos en cantones y provincias
px.treemap(covid_cantonal_positivos, 
           values="positivos", 
           color_discrete_sequence=px.colors.sequential.YlOrRd[::-1],
           path=["provincia", "canton"], # jerarquía de variables
           title="Casos positivos de COVID en provincias y cantones de Costa Rica al 2022-05-30")


# ### *Sunbursts*

# Los *sunbursts* también se utilizan para mostrar datos organizados de manera jerárquica, en formas circulares.
# 
# En plotly.express, los *sunbursts* se implementan con el método [plotly.express.sunburst()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.sunburst.html). Se recomienda revisar el [tutorial](https://plotly.com/python/sunburst-charts/).

# In[32]:


# Surburst de casos positivos en cantones y provincias
px.sunburst(covid_cantonal_positivos, 
            values="positivos", 
            path=["provincia", "canton"],
            title="Casos positivos de COVID en provincias y cantones de Costa Rica al 2022-05-30")


# ### Gráficos de dispersión

# Un [gráfico de dispersión (*scatterplot*)](https://es.wikipedia.org/wiki/Diagrama_de_dispersi%C3%B3n) despliega los valores de dos variables numéricas, como puntos en un sistema de coordenadas. El valor de una variable se despliega en el eje X y el de la otra variable en el eje Y. Variables adicionales pueden ser mostradas mediante atributos de los puntos, tales como su tamaño, color o forma.
# 
# En plotly.express, los gráficos de barras se crean con el método [plotly.express.scatter()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.scatter.html). Se recomienda revisar el [tutorial](https://plotly.com/python/line-and-scatter/).
# 
# Seguidamente, se utiliza un gráfico de dispersión para mostrar las cantidades diarias de pacientes hospitalizados en salón y de pacientes hospitalizados en unidades de cuidados intensivos (UCI) por causa del COVID, del conjunto de datos generales de COVID.

# In[33]:


# Se agrega una columna correspondiente al año,
# para luego utilizarla para colorear los puntos
covid_general["anio"] = pd.DatetimeIndex(covid_general['fecha']).year

# Gráfico de dispersión
px.scatter(covid_general, 
           x="salon", 
           y="uci", 
           color="anio",
           title="Pacientes de COVID hospitalizados en salón vs pacientes hospitalizados en UCI al 2020-05-30",
           labels={"salon":"Pacientes hospitalizados en salón", 
                   "uci":"Pacientes hospitalizados en UCI",
                   "anio":"Año"})


# #### Ejercicios

# 1. En un gráfico de dispersión, muestre las variables de casos positivos y casos fallecidos de COVID, del conjunto de datos generales.

# ### Gráficos de líneas

# Un [gráfico de líneas](https://en.wikipedia.org/wiki/Line_chart) muestra información en la forma de puntos de datos, llamados marcadores (*markers*), conectados por segmentos de líneas rectas. Es similar a un gráfico de dispersión pero, además de los segmentos de línea, tiene la particularidad de que los datos están ordenados, usualmente con respecto al eje X. Los gráficos de línea son usados frecuentemente para mostrar tendencias a través del tiempo.
# 
# En plotly.express, los gráficos de líneas se crean con el método [plotly.express.line()](https://plotly.github.io/plotly.py-docs/generated/plotly.express.line.html). Se recomienda revisar el [tutorial](https://plotly.com/python/line-charts/).

# El siguiente gráfico de líneas muestra la cantidad de casos positivos de COVID acumulados a través del tiempo, de acuerdo con el conjunto de datos generales.

# In[34]:


# Gráfico de líneas
px.line(covid_general, 
        x="fecha", 
        y="positivos",
        color_discrete_sequence=["blue"],
        title="Casos positivos acumulados de COVID en Costa Rica al 2020-05-30",
        labels={"fecha":"Fecha", "positivos":"Casos"})


# El siguiente gráfico le agrega al anterior las variables de casos activos, recuperados y fallecidos. También especifica un color para cada variable.

# In[35]:


# Gráfico de líneas

# Se crea una figura, para luego modificarla
fig = px.line(covid_general, 
              x="fecha", 
              y=["positivos", "activos", "recuperados", "fallecidos"],
              color_discrete_sequence=["blue", "red", "green", "black"],
              title="Casos positivos acumulados de COVID en Costa Rica al 2020-05-30",
              labels={"fecha":"Fecha"})

# Se modifica la leyenda
fig.update_layout(legend=dict(
    title="Casos"
))

# Se modifica el eje y
fig.update_yaxes(title="Casos")

# Se muestra la figura
fig.show()


# #### Ejercicios

# 1. En un gráfico de líneas, muestre las variables de casos positivos de hombres y de casos positivos de mujeres, del conjunto de datos generales de COVID.

# ## Recursos de interés

# - [From data to Viz | Find the graphic you need](https://www.data-to-viz.com/)
# - [Data Visualization as The First and Last Mile of Data Science Plotly Express and Dash | SciPy 2021](https://www.youtube.com/watch?v=FpCgG85g2Hw)
