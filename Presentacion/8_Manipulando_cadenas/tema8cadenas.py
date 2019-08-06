# print('Ejercicio 1')
# ejemplo = 'Mi nombre es Andres'
#
# def conv(frase):
#     nuevo = frase.split()
#     return '_'.join(nuevo)
# print(conv(ejemplo))
#
# def conv1(frase):
#     cad = ''
#     for i in frase:
#         if i == ' ':
#             cad = cad + '_'
#         else:
#             cad = cad + i
#     return cad
# print(conv1(ejemplo))


# print('Ejercicio 2 en diferentes maneras')
# num = '5.6 ,7.23 ,4.23 ,2.98 ,1.11 ,5.45 ,9.38,7.86'
#
# lista = num.split(',')
# sum = 0
# for i in range(len(lista)):
#     lista[i] = float(lista[i])
#     sum = sum + lista[i]
# print(sum)
# print(sum/len(lista))
# print(max(lista))
# print(min(lista))

#
# def cad_a_list(cad):
#     lista = cad.split(',')
#     for i in range(len(lista)):
#         lista[i] = float(lista[i])
#     return lista
#
# def sum_av_max_min(list):
#     sum = 0
#     for i in list:
#         sum += i
#     print(sum)
#     print(sum/len(list))
#     print(max(list))
#     print(min(list))
#
# sum_av_max_min(cad_a_list(num))


#
# def ejercicio(datos):
#     lista = datos.split(',')
#     sum = 0
#     for i in range(len(lista)):
#         lista[i] = float(lista[i])
#         sum = sum + lista[i]
#     print(sum)
#     print(sum/len(lista))
#     print(max(lista))
#     print(min(lista))
#
# ejercicio(num)







