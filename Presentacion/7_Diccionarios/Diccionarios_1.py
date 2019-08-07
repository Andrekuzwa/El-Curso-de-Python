"""COMIENZO"""
# miGato = {'tamano': 'gordo', 'color': 'gris', 'disposicion': 'ruidoso'}
#
# print(miGato['tamano'])
#
# print('Mi gato tiene una piel ' + miGato['color'])

"""DIFERENCIA - Lista o diccionarios"""
"""Lista"""
# miGato = ['huevo', 'platano', 'queso']
# miPerro = ['queso', 'platano', 'huevo']
# miGato == miPerro
"""Diccionarios"""
# miGato = {'huevo', 'platano', 'queso'}
# miPerro = {'queso', 'platano', 'huevo'}
# miGato == miPerro

"""KEYS, VALUES, ITEMS"""

# galloPinto = {'color': 'rojo', 'edad': 65}
#
# for v in galloPinto.values():
#     print(v)
#
# for k in galloPinto.keys():
#     print(k)
#
# for i in galloPinto.items():
#     print(i)

"""GET"""
# frutas = {'maduro': 5, 'pina': 10, 'manzana': 12}
#
# print('Yo tengo ' + str(frutas.get('manzana', 0)) + ' manzanas.')
# print('Yo tengo ' + str(frutas.get('pitaya', 0)) + ' pitaya.')

# """Cumpleanos - TASK"""
# cumpleanos = {'John': 'Apr 1', 'Mark': 'Mar 23', 'George': 'Dec 1', 'Mike': 'Jun 12'}
#
# while True:
#     nombre = input('Introduce el nombre (en blanco para parar)\n:')
#     if nombre == '':
#         break
#
#     if nombre in cumpleanos:
#         print(cumpleanos[nombre] + ' es el cumpleaños de ' + nombre)
#     else:
#         print('No tengo información de cumpleaños sobre ' + nombre)
#         fecha = input(('cuando es su cumpleaños?'))
#         cumpleanos[nombre] = fecha
#         print('Base de datos de cumpleaños actualizada!')
#
# for i in nombre.values():
#     print(i)
#
# for j in nombre.keys():
#     print(j)
#
# for i in nombre.items():
#     print(i)
#
# for k, v in nombre.items():
#     print(v + ' is a birthday of ' + k)

"""SET DEFAULT  ESTABLECER PREDETERMINADO"""
# huevo = {'nombre': 'Mufasa', 'edad': 21}
# print(huevo.items())
#
# huevo.setdefault('color', 'blanco')
# print(huevo.items())
#
# huevo.setdefault('color', 'negro')
# print(huevo.items())

"""Recuento de caracteres"""
#
# mensaje = 'Era un día frío brillante en abril, y los relojes estaban golpeando trece.'
# count = {}
#
# for firmar in mensaje:
#     count.setdefault(firmar, 0)
#     count[firmar] = count[firmar] + 1
# print(count)

"""Diccionario/ lista en el diccionario"""
# picnic = {'Alden': {'manzanas': 2, 'naranjas': 2, 'gallo pinto': 3 },
#           'Mark': {'agua': 4, 'maduro': 4, 'manzanas': 2, 'naranjas': 2},
#           'Alex': {'naranjas': 4, 'pastel': 1 },
#           'David': {'manzanas': 2, 'gallo pinto': 1, 'coca': 4}}
#
# def total(huesped, articulo):
#     numeroTotal = 0
#     for k, v in huesped.items():
#         numeroTotal = numeroTotal + v.get(articulo, 0)
#     return numeroTotal
#
# print('Número de cosas traídas:')
# print(' - Manzanas ' + str(total(picnic, 'manzanas')))
# print(' - Naranjas ' + str(total(picnic, 'naranjas')))
# print(' - Gallo pinto ' + str(total(picnic, 'gallo pinto')))
# print(' - Agua ' + str(total(picnic, 'agua')))
# print(' - Maduro ' + str(total(picnic, 'maduro')))
# print(' - Pastel ' + str(total(picnic, 'pastel')))
# print(' - Coca ' + str(total(picnic, 'coca')))
# print(' - Salchicha ' + str(total(picnic, 'salchicha')))

"""El tres en línea"""

# tablero = {'1': ' ', '2': ' ', '3': ' ',
# #            '4': ' ', '5': ' ', '6': ' ',
# #            '7': ' ', '8': ' ', '9': ' '}
# #
# # def tableroImpresion(tablero):
# #     print(tablero['1'] + '|' + tablero['2'] + '|' + tablero['3'])
# #     print('-+-+-')
# #     print(tablero['4'] + '|' + tablero['5'] + '|' + tablero['6'])
# #     print('-+-+-')
# #     print(tablero['7'] + '|' + tablero['8'] + '|' + tablero['9'])
# #
# # turno = 'X'
# # for i in range(9):
# #     tableroImpresion(tablero)
# #     movimiento = input('Es el turno de ' + turno + '. ¿Mudarse a?\n')
# #     tablero[movimiento] = turno
# #     if turno == 'X':
# #         turno = '0'
# #     else:
# #         turno = 'X'
# #
# # tableroImpresion(tablero)