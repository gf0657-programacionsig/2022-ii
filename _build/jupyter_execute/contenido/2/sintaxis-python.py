#!/usr/bin/env python
# coding: utf-8

# # Sintaxis de Python

# ## Trabajo previo
# 
# ### Lecturas
# Severance, D. C. R. (2016). *Python for Everybody: Exploring Data in Python 3 (chapters 1 - 14)* (S. Blumenberg & E. Hauser, Eds.). CreateSpace Independent Publishing Platform. https://www.py4e.com/html3/
# 
# ### Otros recursos
# [Documentación oficial de Python](https://docs.python.org/)
#   - [Referencia del lenguaje Python](https://docs.python.org/3/reference/i)
#   - [La biblioteca estándar de Python](https://docs.python.org/3/library/index.html#library-index)
#   - [Tutorial de Python](https://docs.python.org/3/tutorial/index.html#tutorial-index)

# ## Resumen
# Este capítulo contiene un resumen de la sintaxis del lenguaje de programación Python.

# ## Comentarios

# Python permite varios tipos de comentarios en el código fuente. Las convenciones generales para su uso se detallan en [PEP 8 -- Style Guide for Python Code - Comments](https://www.python.org/dev/peps/pep-0008/#comments).

# ### De una línea

# Se definen con el símbolo `#` (*hash*). Por ejemplo:

# In[1]:


# Cálculo del índice de masa corporal (IMC)

peso = 73 # peso en kilogramos
estatura = 1.70 # estatura en metros

imc = peso/estatura**2

print("El IMC es {imc:.2f}".format(imc=imc))


# ### De múltiples líneas

# Python no tiene soporte explícito para comentarios de varias líneas. Sin embargo, se pueden implementar de dos formas:

# 1. Con varias líneas iniciadas con `#`:

# In[2]:


# Línea 1
# Línea 2
# Línea 3


# 2. Con bloques de líneas delimitados con `"""` (tres comillas dobles) al inicio y al final:

# In[3]:


"""
Línea 1
Línea 2
Línea 3
"""


# ### docstrings

# Las *docstrings* son una forma de documentar módulos, funciones, clases y métodos de Python. Se agregan debajo del encabezado y están delimitados con `"""` (tres comillas dobles) al inicio y al final.
# 
# Pueden contener una o varias líneas. En este último caso, la primera línea es una descripción corta y es seguida de una línea en blanco, previa a las líneas restantes. Deben iniciar con mayúscula y finalizar con punto.

# *docstring* de una línea:

# In[4]:


def imc(peso, estatura):
    """Cálculo del índice de masa corporal (IMC)."""
    return peso/estatura**2

print(imc.__doc__)


# *docstring* de varias líneas:

# In[5]:


def imc2(peso, estatura):
    """Cálculo del índice de masa corporal (IMC)
    
    El IMC es una razón matemática que asocia el peso y la estatura de un individuo, 
    ideada por el estadístico belga Adolphe Quetelet, 
    por lo que también se conoce como índice de Quetelet. 
    """
    
    return peso/estatura**2

print(imc2.__doc__)


# Varias herramientas pueden generar documentación a partir de *docstrings*. Entre estas, pueden mencionarse [Doxygen](http://www.doxygen.nl/), [pydoc](https://docs.python.org/3/library/pydoc.html) y [Sphinx](https://www.sphinx-doc.org/).
# 
# Las convenciones para el uso de *docstrings* se detallan en [PEP 257 -- Docstring Conventions](https://www.python.org/dev/peps/pep-0257/).

# ## Tipos de datos
# Python puede trabajar con una gran variedad de tipos de datos, entre los que están los siguientes:
# 
# <table>
# 
# <tr><th>Nombre</th><th>Palabra reservada</th><th>Descripción</th></tr>
# 
# <tr><td>Enteros</td><td>int</td><td>Números enteros: 0, 20, -34</td></tr>
# <tr><td>Punto flotante</td><td>float</td><td>Números con punto decimal: 0.1, 35.0, -100.5</td></tr>
# <tr><td>Booleanos</td><td>bool</td><td>Valores lógicos de <strong>True</strong> (verdadero) o <strong>False</strong> (falso)</td></tr>
# <tr><td>Hileras</td><td>str</td><td>Secuencias ordenadas de caracteres: "Python", "Hola mundo"</td></tr>
# <tr><td>Listas</td><td>list</td><td>Secuencias ordenadas de objetos: [1, 2, 3, "cuatro", True, [5, 6, 7]]</td></tr>
# <tr><td>Tuplas</td><td>tuple</td><td>Secuencias ordenadas inmutables de objetos: ("tres", [23, 34], -89, False)</td></tr>
# <tr><td>Conjuntos</td><td>set</td><td>Colecciones no ordenadas de objetos: {1, 2, "a", "b"}</td></tr>
# <tr><td>Diccionarios</td><td>dict</td><td>Pares ordenados atributo:valor: {"nombre":"Juan", "apellido":"Pérez"}</td></tr>
# 
# </table>
# 
# Existen otros tipos de datos más especializados (ej. fechas, horas, enumerados). Todos pueden consultarse en la documentación de la [biblioteca estándar de Python](https://docs.python.org/3/library/index.html#library-index).

# ### La función type()
# La función [type()](https://docs.python.org/3/library/functions.html#type) retorna el tipo del objeto que recibe como argumento.

# In[6]:


type(25)


# In[7]:


type("Costa Rica")


# In[8]:


type([1, 2, 3])


# In[9]:


type(2 > 5)


# ## Variables
# Una variable es un nombre que se asigna a un espacio en la memoria del computador que contiene un valor. El valor se asigna mediante el operador `=`.

# In[10]:


# A la variable x se le asigna el valor 10
x = 10
print(x)
print(type(x))


# In[11]:


# A la variable nombre se le asigna el valor "Patricia"
nombre = "Patricia"
print(nombre)
print(type(nombre))


# In[12]:


# A la variable lista_primos se le asigna una lista de números primos
lista_primos = [2, 3, 5, 7, 11, 13, 17]
print(lista_primos)
print(type(lista_primos))


# In[13]:


# Una variable puede cambiar de valor durante la ejecución del programa
i = 1
print(i)
i = i + 1
print(i)


# In[14]:


# El valor de una variable pueden asignarse con base en los de otras variable
x = 20
y = 10
z = x + y
print(z)


# ### Reglas para los nombres de variables
# - No pueden empezar con un número (sí pueden usarse números en el resto del nombre).
# - No pueden contener espacios (se sugiere usar el guión bajo: `_`).
# - No pueden contener ninguno de los siguientes símbolos: `'",<>:/?|\!@#%^&*~-+`.
# - No deben utilizarse [palabras reservadas de Python](https://docs.python.org/3/reference/lexical_analysis.html#keywords).
# - Se considera una [buena práctica utilizar nombres en minúscula y con guiones bajos](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names), para así mejorar la legibilidad.
# - Es importante utilizar nombres significativos para las variables, que reflejen su propósito.

# Las variables mejoran la legibilidad de los procesos:

# In[15]:


# Cálculo del impuesto de ventas, sin variables
100000 * 0.13


# In[16]:


# Cálculo del impuesto de ventas, con variables

# Entrada
precio_articulo = 100000
tasa_impuesto = 0.13

# Proceso
monto_impuesto = precio_articulo * tasa_impuesto

# Salida
print(monto_impuesto)


# ### Ejercicios

# 1. Utilice variables en un programa que covierta grados Celsius a Fahrenheit. Puede consultar la fórmula en https://www.rapidtables.com/convert/temperature/celsius-to-fahrenheit.html

# In[17]:


# Entrada

# Proceso

# Salida


# 2. Utilice variables en un programa que calcule el índice de masa corporal (IMC). Pueden consultar la fórmula en [https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator](https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator)

# In[18]:


# Entrada

# Proceso

# Salida


# ## Expresiones

# En Python, una [expresión](https://docs.python.org/3/reference/expressions.html) es una combinación de:
# * [Literales](https://docs.python.org/3/reference/lexical_analysis.html#literals): valores constantes de números, hileras, listas, booleanos y otros tipos de datos.
# * Variables.
# * Los dos anteriores combinados mediante [operadores](https://docs.python.org/3/reference/lexical_analysis.html#operators) o funciones.
# 
# **Una expresión tiene un valor numérico, textual, booleano o de otro tipo**. En las secciones siguientes se brindan algunos ejemplos de expresiones.
# 
# **NOTA:** al escribir una expresión en la línea de comandos del interpretador de Python o en un _notebook_, esta retorna su valor. Sin embargo, esto no sucede en un programa. En este último caso, si se quiere visualizar el valor de una expresión, debe imprimirse con la función **print()**, por ejemplo.

# Para los ejemplos siguientes, se definen las variables:

# In[19]:


x = 20
y = 21.5
h = "Python"


# ### Aritméticas

# Se utilizan para realizar operaciones matemáticas con números enteros, complejos o de punto flotante.

# #### Operadores aritméticos
# 
# <table>
# 
# <tr><th>Operador</th><th>Descripción</th><th>Ejemplo</th></tr>
# 
# <tr><td>+</td><td>Suma</td><td>4 + 3 (= 7)</td></tr>
# <tr><td>-</td><td>Resta</td><td>10 - 5 (= 5)</td></tr>
# <tr><td>*</td><td>Multiplicación</td><td>3 * 4 (= 12)</td></tr>
# <tr><td>/</td><td>División</td><td>5 / 2 (= 2.5)</td></tr>
# <tr><td>//</td><td>División entera</td><td>5 // 2 (= 2)</td></tr>
# <tr><td>%</td><td>Módulo</td><td>5 % 2 (= 1)</td></tr>
# <tr><td>**</td><td>Exponenciación</td><td>2 ** 3 (= 8)</td></tr>
# </table>

# #### Ejemplos

# In[20]:


# Literal
0


# In[21]:


# Variable
x


# In[22]:


# Literal, variable, operador aritmético y función
34 + int(y)


# ### Booleanas

# Se les llama también expresiones lógicas. Tienen solamente dos posibles valores:
# * `True` (verdadero)
# * `False` (falso)
# 
# Son sumamente importantes en Python (y en otros lenguajes de programación) porque con base en expresiones boolenanas se construyen sentencias como condicionales y ciclos.

# #### Operadores booleanos

# <table>
# 
# <tr><th>Operador</th><th>Descripción</th><th>Ejemplo</th></tr>
# 
# <tr><td>and</td><td>Retorna <strong>True</strong> si ambos operandos son verdaderos y <strong>False</strong> en caso contrario</td><td>(1 < 2) and (4 > 3) [= True]</td></tr>
# <tr><td>or</td><td>Retorna <strong>True</strong> si al menos uno de los operados es verdadero y <strong>False</strong> en caso contrario</td><td>(10 > 20) or (40 < 30) [= False]</td></tr>
# <tr><td>not</td><td>Retorna <strong>True</strong> si el operando el falso  y <strong>False</strong> en caso contrario</td><td>not (4 > 2) [= False]</td></tr>
# </table>

# #### Operadores relacionales

# Con frecuencia, las expresiones boolenas incluyen operadores relacionales (de comparación).
# <table>
# 
# <tr><th>Operador</th><th>Descripción</th><th>Ejemplo</th></tr>
# 
# <tr><td>==</td><td>Igual</td><td>(3 + 1) == (2 ** 2)</td></tr>
# <tr><td>!=</td><td>Diferente</td><td>0 != 1</td></tr>
# <tr><td>></td><td>Mayor que</td><td>3 > 2</td></tr>
# <tr><td><</td><td>Menor que</td><td>2 < 3</td></tr>
# <tr><td>>=</td><td>Mayor o igual que</td><td>3 >= (2 + 1)</td></tr>
# <tr><td><=</td><td>Menor o igual que</td><td>2 <= 5</td></tr>
# 
# </table>

# #### Ejemplos

# In[23]:


# Literal
True


# In[24]:


# Literal y variable
x == 20


# In[25]:


# Literal, variable y operador
x > 100


# In[26]:


# Literales, variables, operador aritmético y operador relacional
(x + 45) > 10 


# In[27]:


# Literales, variables, operadores aritméticos, operadores relacionales y operadores lógicos
((x + 45) > 10) and ((y - 20) <= 0)


# ### Otras

# In[28]:


# Hileras
"Hola " + h


# In[29]:


# Listas
[1, 2, 3] + ["a", "b", "c"]


# ## Condicionales

# Los condicionales son instrucciones que permiten evaluar condiciones (i.e. expresiones lógicas) y alterar el flujo del programa de acuerdo con su valor.

# ### La sentencia `if`

# En Python, los condicionales se implementan a través de la sentencia [if](https://docs.python.org/3/reference/compound_stmts.html#the-if-statement). En su forma más básica, tiene la siguiente estructura:
# 
# ```python
# if <condición>:
#     <bloque de sentencias>
# ```
# 
# <condición> es una expresión lógica (que es verdadera o falsa). Si la condición es verdadera, se ejecutará el bloque de sentencias que está luego de los dos puntos (:). En Python, un bloque de instrucciones se identifica por la cantidad de espacios que lo tabulan.
# 
# Por ejemplo:

# In[30]:


print("Inicio del programa.")
print("Este programa indica si una persona es menor de edad.")
print("\n")

edad = 15
if edad < 18:
    print("- La persona es MENOR.")
    print("- No puede votar en las elecciones presidenciales.")
    print("- No puede tener licencia para conducir automóviles.")
    
print("\n")    
print("Fin del programa.")


# Después de ejecutar el bloque (si se cumple la condición), el programa continua ejecutando las instrucciones que están fuera del bloque, si es que las hay.

# #### La cláusula `else`

# Es una cláusula opcional que se utiliza para especificar un bloque alterno que se ejecuta si no se cumple la condición del `if`. Tiene la siguiente estructura:
# 
# ```python
# if <condición>:
#     <bloque de sentencias>
# else:
#     <bloque de sentencias>
# ```
# 
# Solamente puede usarse una cláusula else en cada sentencia if. Por ejemplo:

# In[31]:


print("Inicio del programa.")
print("Este programa indica si una persona es menor o adulta.")
print("\n")

edad = 22
if edad < 18:
    print("- La persona es MENOR.")
    print("- No puede votar en las elecciones presidenciales.")
    print("- No puede tener licencia para conducir automóviles.")    
else:
    print("- La persona es ADULTA.")
    print("- Puede votar en las elecciones presidenciales.")
    print("- Puede tener licencia para conducir automóviles.")
    
print("\n")    
print("Fin del programa.")


# #### La cláusula `elif`

# Es una cláusula opcional que permite especificar condiciones adicionales entre las cláusulas `if` y `else`. 
# 
# ```python
# if <condición>:
#     <bloque de sentencias>
# elif <condición>:
#     <bloque de sentencias>
# else:
#     <bloque de sentencias>
# ```    
# 
# Puede usarse cualquier cantidad de cláusulas `elif`. La cláusula `elif` puede utilizarse sin la clásula `else` y viceversa.
# 
# Ejemplo:

# In[32]:


print("Inicio del programa.")
print("Este programa indica si una persona es menor, adulta o adulta mayor.")
print("\n")

edad = 65
if edad < 18:
    print("- La persona es MENOR.")
    print("- No puede votar en las elecciones presidenciales.")
    print("- No puede tener licencia para conducir automóviles.")
elif edad < 65:
    print("- La persona es ADULTA.")
    print("- Puede votar en las elecciones presidenciales.")
    print("- Puede tener licencia para conducir automóviles.")    
else:
    print("- La persona es ADULTA MAYOR.")
    print("- Puede votar en las elecciones presidenciales.")
    print("- Puede tener licencia para conducir automóviles.")
    print("- Tiene acceso gratuito al servicio público de autobuses.")
    print("- Tiene prioridad en las filas de atención en bancos y otros servicios.")
    
print("\n")    
print("Fin del programa.")


# ### Acerca de los bloques en Python

# Los bloques son conjuntos de sentencias contiguas que están tabulados con la misma cantidad de espacios. La cantidad de espacios puede ser decidida por el programador, pero [se recomienda usar cuatro espacios](https://www.python.org/dev/peps/pep-0008/#indentation).
# 
# **NOTA:** deben utilizarse espacios y NO TABULADORES. Si se mezclan espacios y tabuladores, el programa puede comportarse de forma errónea.

# ## Excepciones

# Las [excepciones](https://docs.python.org/3/reference/executionmodel.html#exceptions) son un mecanismo que provee Python para manejar errores o situaciones inesperadas que se producen durante la ejecución de los programas. Mediante este mecanismo, el curso de ejecución del programa se interrumpe cuando ocurre un error y una excepción es "levantada" (_raised_). El control pasa entonces a otro bloque de instrucciones, el cual se encarga de manejar el error.

# ### Las sentencias try y except

# Las sentencias [try](https://docs.python.org/3/reference/compound_stmts.html#try) y [except](https://docs.python.org/3/reference/compound_stmts.html#except) son las que implementan el manejo de excepciones en Python. En el bloque `try` se coloca el código que puede ocasionar que se levante la excepción y en el bloque `except` se ubica el código que maneja la excepción.
# 
# La estructura básica es la siguiente:
# 
# ```python
# try:
#     <bloque de sentencias que puede generar un error>
# except:
#     <bloque de sentencias que maneja el error>
# ``` 
# 
# Por ejemplo, un llamado a la función [float()](https://docs.python.org/3/library/functions.html#float), que convierte una hilera de texto a un número en punto flotante (i.e. decimal), puede ocasionar un error si la hilera de entrada no corresponde a un número.

# In[33]:


x = float("8,5")
x


# El siguiente bloque de código maneja el error mediante un bloque `try except` y evita el mensaje de error que genera el interpretador de Python, sustituyéndolo por uno más amigable.

# In[ ]:


try:
    x = float("8,5")
except:
    print("Por favor utilice un número")


# El siguiente ejemplo maneja el mismo tipo de error. En este caso, la función [input()](https://docs.python.org/3/library/functions.html#input) se utiliza para leer un número desde el teclado.

# ```python
# fahr_hilera = input('Ingrese la temperatura en grados Fahrenheit: ')
# 
# try:
#     fahr = float(fahr_hilera)
#     celsius = (fahr - 32.0) * 5.0 / 9.0
#     print("El equivalente el grados Celsius es: ", celsius)
# except:
#     print('Por favor ingrese un número.')
# ```

# ### Ejercicios

# 1. Reescriba el programa que calcula el IMC y maneje las excepciones que puedan producirse.

# ## Ciclos

# Los ciclos son bloques de instrucciones que se ejecutan varias veces. Para manejar ciclos, Python provee dos mecanismos: la sentencia `while` y la sentencia `for`.

# ### La sentencia `while`

# La setencia [while](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement) se utiliza para ejecutar repetidamente un bloque de instrucciones mientras que una condición sea verdadera. Su estructura básica es:
# 
# ```python
# while <condicion>:
#     <bloque de sentencias>
# ``` 
# 
# Típicamente, en el bloque hay instrucciones que provocan que la condición se vuelva falsa eventualmente y el ciclo termine. De lo contrario, se producirá un **ciclo infinito**. Nótese que si la condición ya es falsa cuando el flujo del programa llega al `while`, el bloque no se ejecutará nunca.

# #### Ejemplos

# In[35]:


# Contador de números en orden ascendente

n = 1
while n <= 5:
    print(n)
    n = n + 1


# In[36]:


# Contador de números en orden descendente

n = 5
while n >= 1:
    print(n)
    n = n - 1


# In[37]:


# Recorrido de una hilera

texto = "Lorem ipsum"

n = 0
while n < len(texto) :
    print(texto[n])
    n = n + 1


# In[38]:


# Validación de entrada de datos

numero = -1
while not(numero >= 5 and numero <= 10) :
    numero = float(input("\nPor favor ingrese un número entre 5 y 10: "))
    if not(numero >= 5 and numero <= 10) :
        print("El número no está entre 5 y 10, por favor inténtelo de nuevo...")
print("¡Gracias!")


# ### La sentencia `for`

# La sentencia [for](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement) se utiliza para iterar sobre los elementos de estructuras de datos como secuencias (ej. hilera, lista, tupla). Su sintaxis puede resumirse de la siguiente manera:
# 
# ```python
# for <variable_iteracion> in <secuencia>:
#     <bloque de sentencias>
# ``` 
# 
# La variable de iteración es una variable que asume el valor del elemento que se procesa en cada iteración.

# #### Ejemplos

# In[39]:


# Recorrido de una lista

alumnos = ['Juan', 'María', 'Pedro']
for alumno in alumnos:
    print("¡Buenos días " + alumno + "!")


# In[40]:


# Recorrido de un rango de números
# La función range(a, b) crea una secuencia de números entre a y b-1.

for numero in range(1, 11):
    print(numero)


# In[41]:


# Cálculo de la cantidad de elementos 

lista = [3, 41, 12, 9, 74, 15]
contador = 0

print("Lista: ", lista)

for item in lista :
    contador += 1 # esto es lo mismo que: contador = contador + 1
print("Cantidad de elementos:", contador)


# In[42]:


# Suma de los elementos de una lista

lista = [3, 41, 12, 9, 74, 15]
suma = 0

print("Lista: ", lista)

for item in lista :
    suma += item
print("Suma de los elementos:", suma)


# ### La sentencia `break`

# La sentencia [break](https://docs.python.org/3/reference/simple_stmts.html#break) finaliza un ciclo y pasa el flujo del programa a la instrucción que sigue al bloque del `while` o del `for`.

# In[43]:


# Busca el primer número de una lista que sea mayor que 20 y sale del ciclo una vez que lo ha encontrado

lista = [3, 41, 12, 9, 74, 15]
print("Lista: ", lista)

for item in lista :
    if item > 20 :
        print("Primer número mayor que 20: ", item)
        break


# ### La sentencia `continue`

# La sentencia [continue](https://docs.python.org/3/reference/simple_stmts.html#continue) interrumpe la iteración actual de un ciclo y continúa con la siguiente. No sale completamente del ciclo, como la sentencia break.

# In[44]:


# Imprime el doble de cada uno de los números mayores que 20 que hay en una lista. 
# Si el número de la iteración es menor o igual que 20, utiliza la sentencia continue para "saltarse" esa iteración.

lista = [3, 41, 12, 9, 74, 15]
print("Lista: ", lista)

for item in lista :
    if item <= 20:
        continue
    print(item * 2)


# ### Ejercicios

# 1. Escriba un programa que calcule el promedio de los números de una lista.
# 2. Escriba un programa que calcule la desviación estándar de los números de una lista.
# 
# (Maneje la lista en una variable)

# ## Funciones

# Las [funciones](https://docs.python.org/3/reference/compound_stmts.html#function-definitions) son conjuntos de sentencias que **tienen un nombre y realizan una tarea específica** como, por ejemplo, un cálculo matemático o un procesamiento de texto. Por lo general, una función recibe datos de entrada, llamados **argumentos**, y **retorna un valor**.
# 
# 
# El uso de funciones tiene múltiples ventajas, entre las que pueden mencionarse:
# 
# - Mejoran la legibilidad de los programas: mediante el uso de nombres significativos para las secciones de código que realizan una tarea.
# - Evitan la duplicidad de código fuente: una función se define una vez y luego pueden ser invocada muchas veces en un programa.
# - Facilitan el mantenimiento de los programas: al realizar las modificaciones en el código de una función, se evita la necesidad de realizarlas en múltiples secciones de un programa.
# - Facilitan la reutilización de código: mediante mecanismos como módulos de funciones (archivos con colecciones de funciones).

# ### Funciones predefinidas

# Python tiene una lista de [funciones predefinidas](https://docs.python.org/3/library/functions.html), de las cuales algunas se han utilizado ya en este curso:

# In[45]:


# type(): tipo de datos de una expresión
type(20)


# In[46]:


# int(): convierte una expresión a un número de tipo entero (int)
int("100")


# In[47]:


# len(): retorna la cantidad de elementos (items) de una hilera, lista 
# u otros tipos de secuencias y de colecciones.
lista_provincias = ["Limón", "Guanacaste", "Puntarenas", "Heredia", "Alajuela", "Cartago", "San José"]
len(lista_provincias)


# In[48]:


# pow(): eleva un número a una potencia
pow(5, 2)


# Estas funciones predefinidas pueden invocarse en cualquier parte de un programa en Python, con solo escribir su nombre y argumentos.

# ### Funciones definidas en módulos de la biblioteca estándar

# La [biblioteca estándar de Python](https://docs.python.org/3/library/) es el conjunto de módulos que se incluye junto con cada distribución de Python, sin necesidad de instalarlos separadamente. Estos módulos proporcionan un conjunto de funciones más especializadas en áreas como matemáticas, multimedios, redes y otras. Para utilizar estas funciones, primero debe importarse el módulo del que forman parte mediante la sentencia [import](https://docs.python.org/3/reference/simple_stmts.html#import). Por ejemplo:

# In[49]:


import math


# La instrucción anterior brinda acceso a las funciones del módulo [math](https://docs.python.org/3/library/math.html), que contiene un conjunto de funciones matemáticas. Por ejemplo:

# In[50]:


# math.factorial(): retorna el factorial de un número
math.factorial(4)


# In[51]:


# math.sqrt(): retorna la raíz cuadrada de un número
math.sqrt(9)


# Nótese que para invocar a estas funciones, debe escribirse antes el nombre del módulo y un punto.

# ### Funciones definidas en módulos de paquetes externos

# No están incluídos en la biblioteca estándar de Python y deben instalarse de acuerdo con el procedimiento definido por sus autores, como por ejemplo con los programas administradores de paquetes [pip](https://pypi.org/project/pip/) y [Conda](https://conda.io/).
# 
# Muchos de estos paquetes se distribuyen a través de repositorios como el [Python Package Index (PyPI)](https://pypi.python.org/), que a la fecha alberga cerca de 400000 proyectos desarrollados por la comunidad de desarrolladores en Python.

# ### Sintaxis para la definición de nuevas funciones

# En Python, el programador puede definir nuevas funciones a través de la palabra reservada `def`, con la siguiente sintaxis:
# 
# ```python
# def <nombre_funcion>(<arg1>, <arg2>, ..., <argn>):
#     <bloque de sentencias>
#     return <valor_retorno>
# ``` 
# 
# - El nombre de la función es elegido por el usuario y sigue las mismas reglas y recomendaciones que en el caso de los nombres de las variables.
# - Los argumentos se especifican entre paréntesis y se separan entre paréntesis. Si la función no tiene argumentos, deben incluirse paréntesis vacíos.
# - La palabra reservada **return** especifica el valor de retorno de la función.

# #### Ejemplos

# In[52]:


# Definición de una función
def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32.0) * 5.0 / 9.0
    return grados_celsius

# Llamados a la función
print(fahrenheit_a_celsius(104))
print(fahrenheit_a_celsius(50))
print(fahrenheit_a_celsius(32))
print(fahrenheit_a_celsius(14))


# ### Ejercicios

# 1. Defina una función llamada celsius_a_fahrenheit() e inclúyala en el programa del ejemplo anterior. Realice algunos llamados de prueba a la nueva función.

# 2. Escriba un programa que:
# * Le solicite al usuario su peso y su estatura.
# * Calcule su índice de masa corporal (IMC).
# * Imprima el valor del índice y si este es considerado bajo (menor que 18.5), normal (entre 18.5 y 25) o alto (mayor o igual que 25).
# 
# Los detalles del cálculo del índice están en [https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator](https://www.diabetes.ca/diabetes-and-you/healthy-living-resources/weight-management/body-mass-index-bmi-calculator).
# 
# Como parte del programa, defina una función llamada `imc()` que retorne el IMC a partir del peso y la estatura y otra función llamada `imc_interpretacion()` que retorne en una hilera si el IMC es bajo, normal o alto.

# ## Programación orientada a objetos

# La [Programación Orientada a Objetos (POO)](https://en.wikipedia.org/wiki/Object-oriented_programming) es un [paradigma de programación](https://en.wikipedia.org/wiki/Programming_paradigm) basado en el concepto de **objeto**. En el contexto de la POO, los objetos son entidades que poseen:
# - **Estado**: implementado con un conjunto de variables llamadas **propiedades**.
# - **Comportamiento**: implementado con un conjunto de funciones llamadas **métodos**.
# 
# Los objetos se agrupan en [clases](https://docs.python.org/3/tutorial/classes.html). Todos los objetos de una clase contienen los mismos métodos y propiedades. Una clase puede verse como una plantilla o “machote” a partir de la cual se crean objetos. A un objeto creado a partir de una clase se le llama también una **instancia** de esa clase.

# In[53]:


# Definición de la clase cuentaBancaria
class cuentaBancaria:
    # Propiedades
    propietario = ""
    balance = 0
    
    # Métodos
    # Constructor de la clase: crea nuevas instancias e inicializa las propiedades
    def __init__(self, propietario, balance):
        self.propietario = propietario
        self.balance = balance
    
    # Método para realizar depósitos
    def depositar(self, monto):
        self.balance = self.balance + monto

    # Método para realizar retiros
    def retirar(self, monto):
        self.balance = self.balance - monto

    # Método para imprimir información
    def imprimirInformacion(self):
        print("Propietario: " + self.propietario + ", Balance: " + str(self.balance))       


# Una vez definida una clase, pueden declararse objetos o instancias de esta. Las instancias pueden invocar métodos de la clase mediante la notación:
# 
# ```python
#     <instancia>.<método>
# ``` 
# 
# A continuación, se presentan algunos ejemplos de instancias de la clase _cuentaBancaria_ y de llamados a sus métodos.

# In[54]:


# Instancia cuenta01
cuenta01 = cuentaBancaria("Juan Pérez", 1000)
cuenta01.depositar(5000)
cuenta01.imprimirInformacion()


# In[55]:


# Instancia cuenta02
cuenta02 = cuentaBancaria("María Pérez", 10000)
cuenta02.depositar(15000)
cuenta02.retirar(24000)
cuenta02.imprimirInformacion()


# ### Objetos y clases predefinidas de Python

# Todos los datos de un programa en Python se representan mediante objetos o por relaciones entre objetos. Los tipos de datos corresponden a las clases de los objetos.

# In[56]:


# Clase int
print(type(234))


# In[57]:


# Clase float
print(type(10.3))


# In[58]:


# Clase bool
print(type(True))


# In[59]:


# Clase list
print(type([True, 23, 20.6, (1, 2, 3)]))


# El que un dato sea un objeto, implica que además de su valor tiene un conjunto de operaciones asociadas (métodos) que se aplican mediante operadores (ej. `+`, `-`, `*`, `%`) o funciones (ej. `len()`, `type()`). Tanto los operadores como las funciones pueden aplicarse en varias clases. Por ejemplo, el operador `+` se usa para `int`, `float`, `str`, `list` y otras clases; `len()` se usa también en varios tipos de datos.

# ## Otros tipos de datos: cadenas de caracteres, secuencias y diccionarios

# ### La clase `str`

# Como ya se ha explicado, la clase [str](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str) se utiliza para representar datos textuales en Python. Esta clase proporciona un conjunto de [métodos](https://docs.python.org/3/library/stdtypes.html#string-methods), de los que se presentan algunos ejemplos a continuación.

# In[60]:


# str.capitalize(): retorna una copia de 'str' con el primer carácter en mayúscula y el resto en minúscula.
'hola'.capitalize()


# In[61]:


# str.lower(): retorna una copia de 'str' con todos los caracteres en minúscula
'HOLA'.lower()


# In[62]:


# str.count(sub[, start[, end]]): retorna el número de hileras no traslapadas de la subhilera 'sub' 
# en el rango [start, end], el cual es opcional, de 'str'.

cita_socrates = 'Yo solo sé, que no sé nada'
cita_socrates.count('sé') # se cuentan todas las ocurrencias de 'sé'


# In[63]:


cita_socrates.count('sé', 0, 10) # se cuentan solo las ocurrencias ubicadas en el rango [0, 10]


# In[64]:


# str.find(sub[, start[, end]]): retorna el índice menor en donde se encuentra 'sub'
# en el rango [start, end] de 'str'

'Yo solo sé, que no sé nada'.find('solo')


# In[65]:


# str.replace(old, new[, count]): retorna una copia de 'str' con todas las ocurrencias
# de la subhilera 'old' reemplazadas por 'new'. 
# Si 'count' es especificado, solo se reemplazan las primeras 'count' ocurrencias de 'old'
cita_socrates.replace("solo", "solamente")


# **Formateo de hileras**
# 
# Se implementa a través del método [str.format()](https://docs.python.org/3/library/stdtypes.html#str.format). Pueden verse varios ejemplos en [https://pyformat.info/](https://pyformat.info/).

# In[66]:


# Formateo de números enteros
'La suma de 3 + 4 es {} y la resta de 10 - 6 es {}'.format(7, 4)


# In[67]:


# Formateo de un número en punto flotante (6 caracteres, 4 después del punto decimal)
'La relación entre la longitud de una circunferencia y su diámetro es {:6.4f}'.format(3.141592653589793)


# In[68]:


# Formateo de fecha y hora
from datetime import datetime
'{:%d/%m/%Y %H:%M}'.format(datetime(2001, 2, 3, 4, 5))


# ### La clase `list`

# La clase [list](https://docs.python.org/3/library/stdtypes.html#lists) implementa secuencias mutables (i.e. modificables) de objetos que se especifican como **ítems separados por comas y encerrados entre paréntesis cuadrados**.
# 
# Se presentan a continuación algunos ejemplos de operaciones y métodos de la clase `list`, los cuales son comunes a todas las clases de [secuencias mutables](https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types):

# In[69]:


lista = [10, 20, 30, 40, 50]


# In[70]:


# Reemplazo de un ítem con base en su posición
lista[2] = 300
lista


# In[71]:


# Borrado de un ítem con base en su posición
del lista[4]
lista


# In[72]:


# list.append(x): agrega 'x' al final de 'list'
lista.append(50)
lista


# In[73]:


# list.insert(i, x): inserta 'x' en al posición 'i'
lista.insert(4, 45)
lista


# ### La clase `dict`

# La clase [dict](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict) (o *diccionario*) implementa un conjunto de pares ordenados de la forma _atributo_:_valor_. Por ejemplo:

# In[74]:


persona = {"cedula":"408730281", "nombre":"Juan", "apellido":"Pérez"}


# Ejemplos de operaciones y métodos de la clase `dict`:

# In[75]:


# Retorno de valor correspondiente a una llave
persona["cedula"]


# In[76]:


# Asignación de un valor a una llave
persona["nombre"] = "María"
persona


# In[77]:


# Verificación de si una llave existe
"apellido" in persona


# In[78]:


# dict.items(): retorna los ítems (pares (llave, valor)) de 'dict'
persona.items()


# In[79]:


# dict.keys(): retorna las llaves de 'dict'
persona.keys()


# In[80]:


# dict.values(): retorna los valores de 'dict'
persona.values()


# In[81]:


# dict.get(key[, default]): retorna el valor de la llave 'key' en 'dict'
persona.get("apellido")


# ## Archivos

# Los archivos proporcionan una forma de almacenar datos de manera persistente (i.e. no volátil) en medios como discos duros, discos compactos, DVD, dispositivos de almacenamiento USB y otros. Contrario a lo que sucede a las estructuras que residen en la memoria del computador, como las variables, la información almacenada en archivos permanece después de que finaliza la ejecución de un programa o se apaga el computador. En Python, los archivos se manejan como objetos de tipo [file](https://docs.python.org/3/glossary.html#term-file-object), los cuales tienen un conjunto de [métodos](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files), entre las que están:
# 
# * [open()](https://docs.python.org/3/library/functions.html#open): para abrir un archivo.  
# * [read()](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files): para leer datos de un archivo.  
# * [write()](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files): para escribir datos en un archivo.  
# * [close()](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects): para cerrar un archivo.
# 
# Estas operaciones se ilustran en la {numref}`figure-operaciones-archivos-python`.
# 
# ```{figure} img/operaciones-archivos-python.png
# :name: figure-operaciones-archivos-python
# 
# Operaciones para manejo de archivos en Python. Fuente: {cite}`severance_py4e_nodate`.
# ```
# 
# Estas operaciones se realizan a través de una variable llamada "manejador de archivo" (*file handle*).

# ### Uso de la sentencia ```with``` para leer y escribir en archivos
# La sentencia [with](https://docs.python.org/3/reference/compound_stmts.html#with) se utiliza para ejecutar un bloque con métodos definidos por un [administrador de contexto (*context manager*)](https://docs.python.org/3/reference/datamodel.html#context-managers). Entre otros usos, permite recorrer un archivo y cerrarlo automáticamente cuando se finaliza.
# 
# El siguiente bloque de código abre un archivo en modo de lectura (```"r"```) con la función open() y recorre e imprime cada una de sus líneas.

# In[82]:


# Recorrido e impresión de las líneas de un archivo de texto
with open("datos/maravillas_antiguas.csv", "r") as archivo:
    for linea in archivo:
        print(linea, end='')


# Para escribir en un archivo, este debe abrirse en modo de escritura (```"w"```).

# In[83]:


# Escritura en un archivo
with open("datos/archivo_nuevo.csv", "w") as archivo:
    archivo.write('Línea 1\n')
    archivo.write('Línea 2\n')
    archivo.write('Línea 3\n')


# ### Archivos CSV
# Los archivos CSV (*comma separated values*, valores separados por comas) son de los más empleados para intercambiar datos en formato tabular (i.e. en columnas). Pueden llamarse de otras formas, como por ejemplo “archivos de texto delimitado”. Son ampliamente utilizados para importar y exportar datos desde y hacia hojas electrónicas, bases de datos y otros sistemas de manejo de información. Consisten de líneas de texto en las cuales hay datos separados por comas. Cada dato corresponde a una columna. Por ejemplo, el siguiente es el contenido de un archivo CSV con cuatro columnas:
# 
# ```
# nombre,ubicacion,longitud,latitud
# Taj Mahal,India,78.042111,27.174799
# Chichen Itza,México,-88.56865,20.6829
# La estatua de Cristo Redentor,Brasil,-43.210556,-22.951944
# ```
# 
# A pesar de ser ampliamente usados, los archivos CSV no son un formato completamente estandarizado, por lo que pueden presentarse con algunas variantes:
# 
# * La primera línea tiene usualmente los nombres de las columnas (llamados también encabezados), pero no siempre.
# * El caracter separador de las columnas no siempre es una coma. Puede ser también un tabulador, un punto y coma, otro carácter o incluso una combinación de caracteres.
# * Las columnas de texto pueden ir encerradas entre comillas para evitar el problema que se presenta si dentro del texto hay una coma u otro carácter separador.
# * El conjunto de caracteres puede sufrir alteraciones cuando se traslada entre herramientas de software o entre sistemas operativos, sobre en todo en caracteres especiales como los acentos.

# #### El módulo ```csv```
# El módulo [csv](https://docs.python.org/3/library/csv.html) facilita el manejo de archivos CSV en Python. Además de leer el archivo línea por línea, las separa en sus respectivas columnas, al representarlas mediante listas. El método [csv.reader()](https://docs.python.org/3/library/csv.html#csv.reader) retorna una lista con las líneas del archivo. Cada línea es, a su vez, una lista de hileras de texto que corresponden a las columnas del archivo.
# 
# El siguiente bloque de código recorre un archivo CSV e imprime sus líneas y las columnas que las componen.

# In[84]:


import csv

# Recorrido e impresión de las líneas de un archivo de texto
with open("datos/maravillas_antiguas.csv") as archivo:
    # Se crea el objeto reader
    lector = csv.reader(archivo)
    
    # Se recorren las líneas
    for linea in lector:
        print('Línea: ', linea)
        
        # Se recorren las columnas de la línea
        for columna in linea:
            print ('Columna: ', columna)


# El método [csv.writer()](https://docs.python.org/3/library/csv.html#csv.writer) se utiliza para escribir en un archivo CSV. El siguiente bloque de código abre un archivo CSV de entrada y recorre sus líneas. Si la columna de ubicación de una línea corresponde a Egipto o Irak, escribe la línea en un archivo de salida.

# In[85]:


import csv

# Recorrido de las líneas de un archivo de texto y escritura en un nuevo archivo de las líneas que cumplen con una condición
with open("datos/maravillas_antiguas.csv") as archivo_entrada:
    lector = csv.reader(archivo_entrada)

    with open("datos/maravillas_antiguas_irak_egipto.csv", "w") as archivo_salida:
        escritor = csv.writer(archivo_salida, delimiter=',')
        i = 0
        for linea in lector:
            if i == 0:
                # Línea del encabezado
                escritor.writerow(linea)
                print(linea)
            elif linea[1] == "Irak" or linea[1] == "Egipto":
                 # La ubicación es Egipto o Irak
                escritor.writerow(linea)
                print(linea)
            i = i + 1


# ### Ejercicios

# Los siguientes ejercicios están basados en el conjunto de datos [Titanic extended dataset (Kaggle + Wikipedia)](https://www.kaggle.com/datasets/pavlofesenko/titanic-extended). 
# 
# 1. Descargue el conjunto de datos y extraiga el archivo CSV con la lista completa de pasajeros (también está disponible en [https://github.com/gf0657-programacionsig/2022-ii/blob/main/contenido/2/datos/kaggle-wikipedia/titanic/pasajeros-titanic-todos.csv](https://github.com/gf0657-programacionsig/2022-ii/blob/main/contenido/2/datos/kaggle-wikipedia/titanic/pasajeros-titanic-todos.csv)).
# 
# 
# 2. Revise la descripción del conjunto de datos y sus propiedades (i.e. columnas).
# 
# 
# 3. Con el módulo `csv`, extraiga en archivos CSV los siguientes subconjuntos de datos y anote la cantidad de registros de cada uno.
# 
# - Hombres y mujeres (en archivos separados).
# - Pasajeros en cada clase (1, 2, 3) (en archivos separados).
# - Pasajeros que sobrevivieron y pasajeros que fallecieron (en archivos separados).
# - Hombres que sobrevivieron y mujeres que sobrevivieron (en archivos separados).
# - Hombres que fallecieron y mujeres que fallecieron (en archivos separados).
# - Pasajeros en cada clase (1, 2, 3) que sobrevivieron y que fallecieron (en archivos separados).
# - Anote la cantidad total de pasajeros que viajaban en el Titanic.
# 
# 
# 4. Con base en la información recopilada, calcule:
# 
# - Proporción de sobrevivientes por sexo.
# - Proporción de sobrevivientes por clase.

# ## Referencias bibliográficas
# ```{bibliography}
# :filter: docname in docnames
# ```

# In[ ]:




