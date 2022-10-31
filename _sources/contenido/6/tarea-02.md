# Tarea 02

## Fecha y hora límite de entrega
Lunes 7 de noviembre de 2022, 07:59 a.m.

## Objetivos
Cada estudiante debe mostrar que es capaz de:

1. Desarrollar programas en Python como cuadernos de notas de Jupyter (*Jupyter notebooks*).
2. Manejar datos con la biblioteca Pandas.
3. Implementar tablas y gráficos con la biblioteca Plotly.
4. Publicar resultados en la Web, junto con el código y los datos que los generan.

## Entregables
Dirección de un repositorio en GitHub que contenga código, datos y documentación. Específicamente:

1. Un cuaderno de notas de Jupyter con el código Python necesario para generar las salidas especificadas en la sección de desarrollo.
2. Un directorio con archivos de datos.
3. Un archivo `README.md` con:
    1. Una breve descripción (no mayor a 200 palabras) del contenido del repositorio. Si lo desea, puede incluir su interpretación de los resultados.
    2. Una mención y un enlace a la fuente de los datos.
    3. Un enlace al sitio con [NBViewer](https://nbviewer.org/) con la visualización del cuaderno de notas con las tablas y gráficos.

La entrega debe realizarse a través de la plataforma Mediación Virtual.

## Consideraciones adicionales
Esta tarea puede realizarse en parejas o de manera individual. Si es en pareja, solo un integrante debe realizar la entrega e indicar el nombre del otro integrante en Mediación Virtual.

## Desarrollo
Debe desarrollar un programa en Python, como un cuaderno de notas de Jupyter, que utilice los datos de COVID en Costa Rica al 30 de mayo de 2022, disponibles en [https://oges.ministeriodesalud.go.cr/](https://oges.ministeriodesalud.go.cr/). Los archivos necesarios son:

- Cantidades diarias de casos a nivel nacional: `05_30_22_CSV_GENERAL.csv`
- Cantidades de casos por cantón: `05_30_22_CSV_POSITIVOS.csv`

Debe cargar los datos en los archivos CSV a data frames de Pandas y prepararlos mediante:

- Conversiones de tipos (ej. fechas).
- Manejo de codificaciones de caracteres (*locales*).
- Eliminación de columnas no necesarias.
- Eliminación de filas no necesarias.
- Cambio de nombres de columnas.

Luego, debe implementar las siguientes salidas con las funciones de la biblioteca Plotly de Python:

1. Una tabla que muestre datos diarios de COVID (del archivo `05_30_22_CSV_GENERAL.csv`). Incluya las columnas: fecha, casos positivos acumulados de hombres (`hom_posi`), casos positivos acumulados de mujeres (`muj_posi`), casos positivos acumulados de menores (`menor_posi`), casos positivos acumulados de adultos (`adul_posi`), casos positivos acumulados de adultos mayores (`am_posi`) y casos positivos nuevos (`nue_posi`). Puede estudiar la manera de implementar tablas en Plotly en [https://plotly.com/python/table/](https://plotly.com/python/table/).

2. Un gráfico de barras que muestre la cantidad de casos positivos nuevos por día. Es decir, debe contener una barra por cada día, desde el 2020-06-03 hasta el 2022-05-30.

3. Un gráfico de líneas que muestre la evolución a través del tiempo de los casos positivos acumulados de hombres y de los casos positivos acumulados de mujeres.

4. Un gráfico de líneas que muestre la evolución a través del tiempo de los casos positivos acumulados de menores, los casos positivos acumulados de adultos y de los casos positivos acumulados de adultos mayores.

5. Una tabla que muestre la cantidad casos positivos en cantones. Incluya las columnas provincia (`provincia`), cantón (`canton`) y casos al 2022-05-30 (`30/05/2022`). No incluya la fila de "Otros" o la que contiene valores nulos. 

6. Un gráfico *sunburst* que muestre, de manera jerárquica, la cantidad de casos positivos en provincias y en los cantones.


Considere este proyecto como un breve artículo de análisis de datos y siga los siguientes lineamientos:

- El código en Python y sus salidas deben ser **legibles y bien presentados**. 
- Procure incluir solamente el código necesario para generar los resultados.
- Agregue texto en Markdown para darle estructura al cuaderno de notas e incluir las explicaciones que considere necesarias.
- Para cada gráfico, incluya un título y etiquetas para los ejes x e y.

## Calificación
Entre paréntesis, se muestra el porcentaje correspondiente a cada aspecto que se calificará:

- Estructura y legibilidad del cuaderno de notas (5%).
- Inclusión de los archivos de datos en el repositorio (5%).
- Inclusión del archivo `README.md`, con el contenido descrito en la sección Entregables (5%).
- Preparación de los archivos de datos (5%).
- Tabla con datos de casos por día (10%).
- Tabla con datos de casos por cantón (10%).
- Gráfico de barras (15%).
- Gráfico de líneas de casos por sexo (15%).
- Gráfico de líneas de casos por edad (15%).
- Gráfico *sunburst* (15%).
