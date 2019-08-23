# """ Módulos integrados """
# print(help('modules'))


""" Módulo OS -------------------------------------------------------------------------------------------------------"""
import os

# Creación de directorios
# os.mkdir("D:\\EL_CURSO_DE_PYTHON")

# Cambio del directorio actual
#os.chdir("D:\\EL_CURSO_DE_PYTHON")

# Obtener el directorio actual
#print(os.getcwd())

""" Módulo de Matemáticas -------------------------------------------------------------------------------------------"""
import math
#from math import e as Euler

# Pie (π)
#print(math.pi)

# Número de Euler
#print(math.e)
#print(Euler)

"""El módulo matemático presenta dos funciones de conversión de ángulo: degrees() y radians(), para convertir 
el ángulo de grados a radianes y viceversa"""

# Grados a radianes
# print(math.radians(180))

# Radianes a grados
# print(math.degrees(math.pi/6))

# SIN (π/2)
# print(math.sin(math.pi/2))

# COS (0)
# print(math.cos(0))

# TAN (30 degrees)
# v = math.radians(30)
# print(math.tan(v))

"""El método math.log10() devuelve el logaritmo base-10 del número dado"""

# print(math.log10(10))

"""El método math.exp() devuelve un número después de elevar e (Euler) al número dado"""

# print(math.e**10)

"""El método math.pow() reciba dos argumentos, eleva el primero al potencia  de segundo y devuelve el resultado."""

# print(math.pow(2, 8))

"""El método math.sqrt() devuelve la raíz cuadrada de un número determinado."""

# print(math.sqrt(36))

"""La función ceil() se aproxima al número dado al entero más pequeño, mayor o igual que el número de punto flotante
dado. La función floor() devuelve el entero más grande menor o igual que el número dado."""

# print(math.ceil(4.5867))

# print(math.floor(4.5867))

""" El módulo de estadísticas ---------------------------------------------------------------------------------------"""
import statistics

"""El método mean() calcula la media aritmética de los números de una lista"""
# print(statistics.mean([2,5,6,9]))

"""El método median() devuelve el valor medio de los datos numéricos de una lista."""
# print(statistics.median([1,2,3,8,9]))

# print(statistics.median([1,2,3,7,8,9]))

"""El método mode() devuelve el punto de datos más común de la lista."""

# print(statistics.mode([2,5,3,2,8,3,9,4,2,5,6]))

"""El método stdev() calcula la desviación estándar en una muestra determinada en forma de lista."""

# print(statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5]))

"""Python - Módulo RANDOM -----------------------------------------------------------------------------------------="""
import random

"""random.random(): Genera un número de flotador aleatorio entre 0,0 y 1,0. La función no necesita argumentos"""

# print(random.random())

"""random.randint(): Devuelve un entero aleatorio entre los enteros especificados."""

# print(random.randint(5, 10))

"""random.randrange(): Devuelve un elemento seleccionado aleatoriamente del intervalo creado por los
argumentos start, stop y step."""

# print(random.randrange(10))

# print(random.randrange(20, 100, 10))

"""random.choice(): Devuelve un elemento seleccionado aleatoriamente de una secuencia no vacía"""

# print(random.choice('carretera'))

# print(random.choice([12,23,45,67,65,43]))

"""random.shuffle(): Esta función reordena aleatoriamente los elementos de una lista"""

# numeros = [12, 23, 45, 67, 65, 43]
# print(numeros)
# random.shuffle(numeros)
# print(numeros)

# random.shuffle(numeros)
# print(numeros)
