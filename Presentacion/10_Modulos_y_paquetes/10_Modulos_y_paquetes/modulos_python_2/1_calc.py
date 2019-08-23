import modulos_python_2.dato.circunferencia

modulos_python_2.dato.circunferencia.circunferencia_de_un_circulo(4)
modulos_python_2.dato.circunferencia.circunferencia_de_un_cuadrado(4)
modulos_python_2.dato.circunferencia.circunferencia_de_un_rectangular(4, 10)

from modulos_python_2.dato.circunferencia import circunferencia_de_un_circulo, circunferencia_de_un_rectangular, \
    circunferencia_de_un_cuadrado  # import *

circunferencia_de_un_circulo(4)
circunferencia_de_un_cuadrado(4)
circunferencia_de_un_rectangular(4, 10)

from modulos_python_2.dato.circunferencia import circunferencia_de_un_circulo as circ_circ, \
    circunferencia_de_un_cuadrado as circ_cuad, circunferencia_de_un_rectangular as circ_rect

circ_circ(4)
circ_cuad(4)
circ_rect(4, 10)


from modulos_python_2.dato.areas import *

print(area_del_circulo(4))
print(area_del_plaza(10))
print(area_del_rectangular(15, 10))
