## Módulos y paquetes

La programación modular se refiere al proceso de dividir una tarea de programación grande y difícil de manejar en subtareas o módulos separados, más pequeños y más manejables. Los módulos individuales se pueden unir como bloques de creación para crear una aplicación más grande.

Hay varias ventajas de modular el código en una aplicación grande:
* Simplicidad: En lugar de centrarse en todo el problema en cuestión, un módulo normalmente se centra en una porción relativamente pequeña del problema
* Reutilización: La funcionalidad definida en un solo módulo puede ser reutilizada fácilmente por otras partes de la aplicación. Esto elimina la necesidad de volver a crear código duplicado.
* Scoping: los módulos suele definir un espacio de nombres independiente, lo que ayuda a evitar colisiones entre identificadores en diferentes áreas de un programa.

En realidad, hay tres maneras diferentes de definir un módulo en Python:
* Un módulo integrado está intrínsecamente contenido en el intérprete, como el módulo itertools.

* Un módulo se puede escribir en lenguaje C y cargar dinámicamente en tiempo de ejecución, como el módulo re (regular expression).

* Un módulo se puede escribir en Python.

##### El contenido de un módulo se accede de la misma manera en los tres casos: con la instrucción "import".

##### Un módulo puede contener varios objetos, como clases, funciones, variables, etc. Un paquete puede contener uno o más módulos relevantes. Físicamente, un paquete es una carpeta que contiene uno o más archivos de módulo.


##### Funciones integradas

El intérprete de Python tiene una serie de funciones integradas. Se cargan automáticamente a medida que se inicia el intérprete y siempre están disponibles. Muchos de ellos han sido discutidos en lecciones anteriores. Por ejemplo, print() y input(), range(), len() y las funciones de conversión de números int(), float(). 


*PLIK "entrance" --- 1_Funciones integradas.py*

abs() | complex() | sum() | sorted() | format() | reversed() | dict() | enumerate()

##### Los módulos integrados

*PLIK "entrance" --- 2_Funciones integradas.py*

Además de las funciones integradas, un gran número de funciones predefinidas también están disponibles como parte de las bibliotecas incluidas con distribuciones de Python.

:blue_heart: Python - Módulo OS

Es posible realizar automáticamente muchas tareas del sistema operativo. El módulo del sistema operativo en Python proporciona funciones para crear y eliminar un directorio (carpeta), capturar su contenido, cambiar e identificar el directorio actual, etc.

:blue_heart: Python - Módulo de Matemáticas

Algunas de las funciones matemáticas más populares se definen en el módulo de matemáticas. Estos incluyen funciones trigonométricas, funciones de representación, funciones logarítmicas, funciones de conversión de ángulo, etc.

:blue_heart: Python - Módulo de Estadísticas

El módulo de estadísticas proporciona funciones a las estadísticas matemáticas de datos numéricos.

:blue_heart: Módulo RANDOM 

The functions of the random module depend on a pseudorandom number generator function, which generates a random float number between 0.0 and 1.0.

##### Módulos escritos en python

Lo bueno de los módulos escritos en Python es que son extremadamente fáciles de construir. Todo lo que necesita hacer es crear un archivo que contenga código legítimo de Python y luego darle un nombre al archivo con una extensión .py.

*pliki do zaprezentowania modułów:*

*modulos_python_1 - bez paczek*  

*modulos_python_2 - z paczkami*

*- ZADANIA -*






















