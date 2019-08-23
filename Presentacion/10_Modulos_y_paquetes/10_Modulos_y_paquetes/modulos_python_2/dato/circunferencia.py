import math


def circunferencia_de_un_circulo(radio):
    circunferencia = 2 * math.pi * radio
    print(str(circunferencia))


def circunferencia_de_un_cuadrado(lado):
    circunferencia = lado * 4
    print(str(circunferencia))


def circunferencia_de_un_rectangular(lado_1, lado_2):
    circunferencia = (lado_1 * 2) + (lado_2 * 2)
    print(str(circunferencia))
