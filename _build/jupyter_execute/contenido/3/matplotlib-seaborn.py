#!/usr/bin/env python
# coding: utf-8

# # Visualización de datos con matplotlib y seaborn

# ## Descripción general

# [matplotlib](https://matplotlib.org/) es una biblioteca para crear visualizaciones de datos estáticas, animadas e interactivas en Python. Su desarrollo fue liderado por John D. Hunter y Michael Droettboom. Su primera versión se liberó en 2003. Le brinda al programador control sobre todos los detalles de un gráfico estadístico. El módulo [pyplot](https://matplotlib.org/stable/tutorials/introductory/pyplot.html), uno de los más populares de matplotlib, proporciona una interfaz de programación similar a la de [MATLAB](https://es.wikipedia.org/wiki/MATLAB). matplotlib es una de las bibliotecas más populares de graficación de Python y puede trabajar independientemente o de manera integrada con [pandas](https://pandas.pydata.org/).
# 
# [seaborn](https://seaborn.pydata.org/) es otra biblioteca para visualización de datos. Implementa una interfaz de alto nivel para matplotlib, con el objetivo de hacerla más fácil de utilizar y mejorar el estilo (colores, formas, etc.) de los gráficos estadísticos.

# ## Instalación de las bibliotecas

# Ambas bibliotecas pueden instalarse con `pip`, `conda` o `mamba`, desde la línea de comandos del sistema operativo.

# Instalación de matplotlib:

# ```
# # Con pip:
# pip install matplotlib
# 
# # Con conda:
# conda install matplotlib -c conda-forge
# 
# # Con mamba:
# mamba install matplotlib -c conda-forge
# ```

# Instalación de seaborn:

# ```
# # Con pip:
# pip install seaborn
# 
# # Con conda:
# conda install seaborn -c conda-forge
# 
# # Con mamba:
# mamba install seaborn -c conda-forge
# ```

# ## Carga de las bibliotecas

# In[1]:


# Carga de módulos de matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import matplotlib.pyplot as plt

# Carga de seaborn
import seaborn as sns

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

# Las siguientes visualizaciones se implementan con los métodos de matplotlib integrados en pandas. pandas puede utilizar varias bibliotecas de graficación y matplotlib es la que emplea por defecto. Los gráficos resultantes se complementan con el módulo pyplot, para aspectos como títulos, tamaños y otros.
# 
# Se desarrollan también algunos ejemplos con seaborn.

# ### Histogramas

# Un [histograma](https://es.wikipedia.org/wiki/Histograma) es una representación gráfica de la distribución de una variable numérica en forma de barras (llamadas en inglés *bins*). La longitud de cada barra representa la frecuencia de un rango de valores de la variable. La graficación de la distribución de las variables es, frecuentemente, una de las primeras tareas que se realiza cuando se explora un conjunto de datos.
# 
# En pandas, los histogramas se crean con el método [pandas.DataFrame.hist()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html). Elementos adicionales del gráfico, como el título y las etiquetas de los ejes, pueden agregarse con matplotlib.pyplot.

# El siguiente histograma muestra la distribución de la variable correspondiente a los casos de COVID positivos en los cantones de Costa Rica.

# In[13]:


# Histograma de casos positivos en cantones
covid_cantonal_positivos["positivos"].hist(
    bins=8,
    color="blue",
    alpha=0.7)

# Título y etiquetas en los ejes
plt.title("Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30")
plt.xlabel("Casos")
plt.ylabel("Frecuencia")


# El método [seaborn.histplot()](https://seaborn.pydata.org/generated/seaborn.histplot.html) permite crear histogramas con seaborn. El argumento `kde` se utiliza para añadir una estimación de densidad del kernel (*Kernel Density Estimation*, KDE), una curva que muestra la densidad de los datos.

# In[14]:


# Histograma y curva de densidad
sns.histplot(data=covid_cantonal_positivos, x="positivos", bins=8, kde=True)

# Título y etiquetas en los ejes
plt.title("Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30")
plt.xlabel("Casos")
plt.ylabel("Frecuencia")


# El argumento `hue` se usa para mostrar una división de cada *bin* de acuerdo con el valor de alguna columna.

# In[15]:


# Histograma con "bins" divididos por provincia 
sns.histplot(data=covid_cantonal_positivos, 
             x="positivos", 
             bins=8, 
             hue="provincia", 
             alpha=0.3)

# Título y etiquetas en los ejes
plt.title("Distribución de la cantidad de casos positivos de COVID en cantones de Costa Rica al 2022-05-30")
plt.xlabel("Casos")
plt.ylabel("Frecuencia")


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
# En pandas, los gráficos de caja se crean con el método [pandas.DataFrame.boxplot()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html).

# El siguiente diagrama de caja muestra la distribución de la variable correspondiente a los casos de COVID fallecidos en los cantones de Costa Rica.

# In[16]:


# Gráfico de caja de casos fallecidos en cantones
covid_cantonal_fallecidos.boxplot(column="fallecidos")

# Título y etiquetas en los ejes
plt.title("Distribución de la cantidad de casos fallecidos de COVID en cantones de Costa Rica al 2022-05-30")
plt.ylabel("Casos")


# El argumento `by` puede utilizarse para agrupar los datos por una variable adicional, como la provincia.

# In[17]:


# Gráfico de caja de casos fallecidos en cantones, agrupados por provincia
covid_cantonal_fallecidos.boxplot(column="fallecidos", by="provincia")

# Título y etiquetas en los ejes
plt.title("Distribución de la cantidad de casos fallecidos de COVID en cantones de Costa Rica al 2022-05-30")
plt.xlabel("Provincia")
plt.ylabel("Casos")


# El método [seaborn.boxplot()](https://seaborn.pydata.org/generated/seaborn.boxplot.html) permite crear gráficos de caja con seaborn.

# In[18]:


# Gráfico de caja de casos fallecidos en cantones agrupados por provincia
sns.boxplot(y=covid_cantonal_fallecidos["fallecidos"], 
            x=covid_cantonal_fallecidos["provincia"])

# Título y etiquetas en los ejes
plt.title("Distribución de la cantidad de casos fallecidos de COVID en cantones de Costa Rica al 2022-05-30")
plt.xlabel("Provincia")
plt.ylabel("Casos")


# #### Ejercicios

# 1. Construya un gráfico de caja de la edad de los pasajeros del Titanic.
# 2. Agregue la distribución de la variable de sobrevivencia al gráfico del ejercicio anterior.
# 
# 3. Construya un gráfico de caja de la cantidad de padres e hijos que viajaban con los pasajeros del Titanic.
# 4. Agregue la distribución de la variable de sobrevivencia al gráfico del ejercicio anterior.
# 
# 5. Construya un gráfico de caja de la cantidad de hermanos y cónyugues que viajaban con los pasajeros del Titanic.
# 6. Agregue la distribución de la variable de sobrevivencia al gráfico del ejercicio anterior.

# ### Gráficos de barras

# Un [gráfico de barras](https://es.wikipedia.org/wiki/Diagrama_de_barras) se compone de barras rectangulares con longitud proporcional a estadísticas (ej. frecuencias, promedios, mínimos, máximos) asociadas a una variable categórica o discreta. Las barras pueden ser horizontales o verticales y se recomienda que estén ordenadas según su longitud, a menos que exista un orden inherente a la variable (ej. el orden de los días de la semana o de los meses del año).

# En pandas, los gráficos de barras se crean con los métodos [pandas.DataFrame.plot.bar()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html), para barras verticales, y [pandas.DataFrame.plot.barh()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html), para barras horizontales.

# El siguiente gráfico de barras verticales muestra las cantidades de casos positivos en los cantones de Limón.

# In[19]:


# Subconjunto de cantones de la provincia de Limón
covid_limon_positivos = covid_cantonal_positivos[covid_cantonal_positivos["provincia"] == "Limón"]

# Se establece la columna "canton" como índice del dataframe
# y este se ordena por la cantidad de casos positivos antes de
# hacer el gráfico con plot.bar()
covid_limon_positivos.set_index("canton") \
                     .sort_values(by="positivos", ascending=False) \
                     .plot.bar()

plt.title("Cantidad de casos positivos de COVID en los cantones de Limón al 2022-05-30")
plt.xlabel("Cantón")
plt.ylabel("Casos")


# El siguiente gráfico de barras horizontales muestra las cantidades de casos activos en los cantones de San José.

# In[20]:


# Subconjunto de cantones de la provincia de San José
covid_sanjose_activos = covid_cantonal_activos[covid_cantonal_activos["provincia"] == "San José"]

# Se establece la columna "canton" como índice del dataframe
# y este se ordena por la cantidad de casos antes de
# hacer el gráfico con plot.barh().
# También se establece el tamaño del gráfico con figsize()
covid_sanjose_activos.set_index("canton").sort_values(by="activos").plot.barh(color="red", figsize=(10, 8))

plt.title("Cantidad de casos activos de COVID en los cantones de San José al 2022-05-30")
plt.xlabel("Cantón")
plt.ylabel("Casos")


# En el siguiente ejemplo, se utiliza el método [pandas.DataFrame.groupby()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html) para agrupar los datos por provincia y sumar los casos positivos.

# In[21]:


# Suma de casos positivos por provincia
covid_provincial_positivos = covid_cantonal_positivos.groupby(["provincia"], as_index=False)["positivos"] \
                                                     .sum()
covid_provincial_positivos

# Se establece la columna "provincia" como índice del dataframe
# y este se ordena por la cantidad de casos positivos antes de
# hacer el gráfico con plot.bar()
covid_provincial_positivos.set_index("provincia") \
                          .sort_values(by="positivos", ascending=False) \
                          .plot.bar()

plt.title("Cantidad de casos positivos de COVID en las provincias de Costa Rica al 2022-05-30")
plt.xlabel("Provincia")
plt.ylabel("Casos")


# El método [seaborn.barplot()](https://seaborn.pydata.org/generated/seaborn.barplot.html) permite crear gráficos de barras con seaborn.

# El siguiente gráfico muestra la proporción de sobrevivientes por sexo y clase entre los pasajeros del Titanic.

# In[22]:


# Gráfico de barras
sns.barplot(data=titanic, x="Sex", y="Survived", hue="Pclass")

plt.title("Proporción de sobrevivientes del Titanic por sexo y clase")
plt.xlabel("Sexo")
plt.ylabel("Proporción de sobrevivientes")


# #### Ejercicios

# 1. Convierta el gráfico de barras del ejemplo de proporción de sobrevivientes por sexo y clase entre los pasajeros del Titanic, en un gráfico de barras apiladas.

# ### Gráficos de pastel

# Un [gráfico de pastel](https://es.wikipedia.org/wiki/Gr%C3%A1fico_circular) representa porcentajes y porciones en secciones (*slices*) de un círculo. Son muy populares, pero también criticados debido a la dificultad del cerebro humano de comparar áreas de sectores circulares, por lo que algunos expertos recomiendan sustituirlos por otros tipos de gráficos como, por ejemplo, gráficos de barras.

# En pandas, los gráficos de barras se crean con el método [pandas.DataFrame.plot.pie()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html).

# El siguiente gráfico de barras verticales muestra las cantidades de casos positivos en los cantones de Limón.

# In[23]:


# Subconjunto de cantones de la provincia de Limón
covid_limon_positivos = covid_cantonal_positivos[covid_cantonal_positivos["provincia"] == "Limón"]

# Se establece la columna "canton" como índice del dataframe
# y este se ordena por la cantidad de casos positivos antes de
# hacer el gráfico con plot.bar()
covid_limon_positivos.set_index("canton") \
                     .sort_values(by="positivos", ascending=False) \
                     .plot.pie(y="positivos", autopct="%1.0f%%")

plt.title("Porcentaje de casos positivos de COVID en los cantones de Limón al 2022-05-30")
plt.ylabel("")
plt.legend(bbox_to_anchor=(1.0, 1.0))


# Seaborn no cuenta con un método para dibujar gráficos de pastel. Sin embargo, para aprovechas las capacidades de esta biblioteca, puede crearse el gráfico con matplotlib y utilizar uno de los esquemas de colores de seaborn con el método [seaborn.color_palette()](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette). Para más información sobre el manejo de colores en seaborn, puede consultar [Choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html).

# In[24]:


# Suma de casos positivos por provincia
covid_provincial_positivos = covid_cantonal_positivos.groupby(["provincia"], as_index=False)["positivos"].sum()
covid_provincial_positivos

# Paleta de colores de seaborn
colores = sns.color_palette('deep')[0:7]
# colores = sns.color_palette('muted')[0:7]
# colores = sns.color_palette('bright')[0:7]
# colores = sns.color_palette('pastel')[0:7]
# colores = sns.color_palette('dark')[0:7]
# colores = sns.color_palette('colorblind')[0:7]


# Se establece la columna "provincia" como índice del dataframe
# y este se ordena por la cantidad de casos positivos antes de
# hacer el gráfico con plot.bar()
covid_provincial_positivos.set_index("provincia") \
                          .sort_values(by="positivos", ascending=False) \
                          .plot \
                          .pie(y="positivos", autopct="%1.0f%%", colors = colores)

plt.title("Procentaje de casos positivos de COVID en provincias al 2022-05-30")
plt.ylabel("")
plt.legend(bbox_to_anchor=(1.0, 1.0))


# #### Ejercicios

# 1. Construya un gráfico de pastel que muestre la proporción de pasajeros sobrevivientes y fallecidos que viajaban en el Titanic.
# 2. Construya un gráfico de pastel que muestre la proporción de cada sexo (masculino, femenino) de pasajeros que viajaban en el Titanic.
# 3. Construya un gráfico de pastel que muestre la proporción de cada clase de pasajeros (1, 2, 3) que viajaban en el Titanic.

# ### Gráficos de dispersión

# Un [gráfico de dispersión (*scatterplot*)](https://es.wikipedia.org/wiki/Diagrama_de_dispersi%C3%B3n) despliega los valores de dos variables numéricas, como puntos en un sistema de coordenadas. El valor de una variable se despliega en el eje X y el de la otra variable en el eje Y. Variables adicionales pueden ser mostradas mediante atributos de los puntos, tales como su tamaño, color o forma.
# 
# En pandas, los gráficos de barras se crean con el método [pandas.DataFrame.plot.scatter()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html).
# 
# Seguidamente, se utiliza un gráfico de dispersión para mostrar las cantidades diarias de pacientes hospitalizados en salón y de pacientes hospitalizados en unidades de cuidados intensivos (UCI) por causa del COVID, del conjunto de datos generales de COVID.

# In[25]:


# Se agrega una columna correspondiente al año,
# para luego utilizarla para colorear los puntos
covid_general["anio"] = pd.DatetimeIndex(covid_general['fecha']).year

# Gráfico de dispersión
covid_general.plot.scatter(x="salon", y="uci", c="anio", colormap="viridis")

plt.title("Pacientes de COVID hospitalizados en salón vs pacientes hospitalizados en UCI al 2020-05-30")
plt.xlabel("Pacientes hospitalizados en salón")
plt.ylabel("Pacientes hospitalizados en UCI")


# El método [seaborn.scatterplot()](https://seaborn.pydata.org/generated/seaborn.scatterplot.html) permite crear gráficos de dispersión con seaborn.
# 
# El mismo gráfico del ejemplo anterior se presenta seguidamente, generado con seaborn.

# In[26]:


# Gráfico de dispersión
sns.scatterplot(data=covid_general, x="salon", y="uci", hue="anio", palette="deep")

plt.title("Pacientes de COVID hospitalizados en salón vs pacientes hospitalizados en UCI al 2020-05-30")
plt.xlabel("Pacientes hospitalizados en salón")
plt.ylabel("Pacientes hospitalizados en UCI")


# El método [seaborn.lmplot](https://seaborn.pydata.org/generated/seaborn.lmplot.html) grafica un modelo de regresión, que permite apreciar más fácilmente tendencias en los datos.

# In[27]:


# Gráfico de dispersión y modelo de regresión
sns.lmplot(data=covid_general, 
           x="salon", 
           y="uci", 
           lowess=True, 
           hue="anio", 
           palette="deep",
           line_kws={"color": "black"})

plt.title("Pacientes de COVID hospitalizados en salón vs pacientes hospitalizados en UCI al 2020-05-30")
plt.xlabel("Pacientes hospitalizados en salón")
plt.ylabel("Pacientes hospitalizados en UCI")


# #### Ejercicios

# 1. En un gráfico de dispersión, muestre las variables de casos positivos y casos fallecidos de COVID, del conjunto de datos generales.

# ### Gráficos de líneas

# Un [gráfico de líneas](https://en.wikipedia.org/wiki/Line_chart) muestra información en la forma de puntos de datos, llamados marcadores (*markers*), conectados por segmentos de líneas rectas. Es similar a un gráfico de dispersión pero, además de los segmentos de línea, tiene la particularidad de que los datos están ordenados, usualmente con respecto al eje X. Los gráficos de línea son usados frecuentemente para mostrar tendencias a través del tiempo.
# 
# En pandas, los gráficos de líneas se crean con el método [pandas.DataFrame.plot.line()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html).

# El siguiente gráfico de líneas muestra la cantidad de casos positivos de COVID acumulados a través del tiempo, de acuerdo con el conjunto de datos generales.

# In[28]:


# Gráfico de líneas
covid_general.plot.line(x="fecha", y=["positivos"])

plt.title("Casos positivos acumulados de COVID en Costa Rica al 2020-05-30")
plt.xlabel("Fecha")
plt.ylabel("Casos positivos")


# El siguiente gráfico le agrega al anterior las variables de casos activos, recuperados y fallecidos. También especifica un color para cada variable.

# In[29]:


# Gráfico de líneas
covid_general.plot.line(x="fecha", 
                        y=["positivos", "activos", "recuperados", "fallecidos"],
                        color={"positivos": "blue", 
                               "activos": "red", 
                               "recuperados": "green", 
                               "fallecidos": "black"}
                       )

plt.title("Casos positivos acumulados de COVID en Costa Rica al 2020-05-30")
plt.xlabel("Fecha")
plt.ylabel("Casos")


# In[30]:


# Gráfico de líneas
sns.lineplot(data=covid_general, x="fecha", y="positivos", color="blue")
sns.lineplot(data=covid_general, x="fecha", y="activos", color="red")
sns.lineplot(data=covid_general, x="fecha", y="recuperados", color="green")
sns.lineplot(data=covid_general, x="fecha", y="fallecidos", color="black")

plt.title("Casos positivos acumulados de COVID en Costa Rica al 2020-05-30")
plt.xlabel("Fecha")
plt.ylabel("Casos")
plt.rcParams["figure.figsize"] = [10, 10]


# El método [seaborn.lineplot()](https://seaborn.pydata.org/generated/seaborn.lineplot.html) permite crear gráficos de líneas con seaborn.
# 
# El mismo gráfico del ejemplo anterior se presenta seguidamente, generado con seaborn.

# #### Ejercicios

# 1. En un gráfico de líneas, muestre las variables de casos positivos de hombres y de casos positivos de mujeres, del conjunto de datos generales de COVID.

# ## Recursos de interés

# [From data to Viz | Find the graphic you need](https://www.data-to-viz.com/)
