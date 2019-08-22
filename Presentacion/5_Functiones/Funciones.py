"""mi_primera_funcion"""
"""Escriba la función llamada "mi primera funcion" que imprime bienvenida, y desea un buen día."""

# def mi_primera_funcion():
#     print("Hi! \nDisfruta tu dia!")
#
# mi_primera_funcion()

"""mi_primera_funcion_con_argumento"""
"""Ingrese la función llamada "my first function_con_argumento" que tiene el nombre como argumento. 
Imprime un saludo con esta persona."""

# def mi_primera_funcion_con_argumento(nombre):
#     print("Hola " + nombre + "!")
#     print("Disfruta tu dia!")
#
# mi_primera_funcion_con_argumento("Alvin")
# mi_primera_funcion_con_argumento("Andre")
# mi_primera_funcion_con_argumento("Ryszard")

"""area_del_circulo"""
"""Cree la función que calcula el área del círculo pasando el radio como argumento e imprime el resultado. 
El parámetro debe proporcionarse como entrada (input)"""

# def area_del_circulo(radio):
#     print(str(3.142 * radio * radio))
#
# area_del_circulo(int(input("Introduzca el número \n:")))


"""La secuencia de Collatz """
# def collatz(numero):
#     print(str(numero))
#     while numero != 1:
#         if numero % 2 == 0:
#             numero = (numero // 2)
#             print(str(numero))
#
#         elif numero % 2 == 1:
#             numero = (3 * numero) + 1
#             print(str(numero))
#
# x = input('Ingrese el número, por favor \n: ')
#
# collatz(int(x))

# # Puntaje final de clases
#
# def carta (nombre, puntuacion):
#     print('¡Hola ' + nombre + '\n')
#     print('Después de todo el semestre académico, hay un tiempo para el resumen.')
#     print('Estoy feliz de que hayas participado en mi curso, espero que hayas disfrutado y aprendido.')
#     print('Tu nota final es:', puntuacion)
#     if int(puntuacion) >= 90:
#         print('¡Lo hiciste excepcionalmente bien! ¡Te deseo lo mejor!')
#     elif int(puntuacion) > 80:
#         print('¡Tu puntaje es realmente bueno! Estoy muy feliz de eso!')
#     elif int(puntuacion) > 70:
#         print('¡Pasaste, pero sé que puedes hacerlo mejor!')
#     else:
#         print('''Desafortunadamente no aprobaste el curso, pero hay un examen de corrección en el que
# puedes participar.'''
#               ' Es el próximo viernes 24 de junio a las 10 en punto.')
#     print('\nSaludos cordiales\n')
#     print('Mejor profesor')
#
# carta('Jacob', '92')
# carta('Alden', '85')
# carta('Leon', '74')
# carta('George', '55')