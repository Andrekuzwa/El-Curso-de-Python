import math


def area_del_circulo(radio):
    area = math.pi * (radio**2)
    return area


def area_del_plaza(lado):
    area = lado ** 2
    return area


def area_del_rectangular(lado_1, lado_2):
    area = lado_1 * lado_2
    return area
