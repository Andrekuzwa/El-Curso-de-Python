# 1
# spam = ['cos','costam','huehe']
#
# def convert(lista):
#     cad = ''
#     for i in range(len(lista)-1):
#         cad = cad + lista[i] + ', '
#     cad = cad + lista[-1]
#     return cad
# print(convert(spam))



#2
# a = [1,2,3,4,5,6,6]
# b = [2,4,6,6,6,6,6]
# def common(list1,list2):
#     list=[]
#     for i in a:
#         for j in b:
#             if i == j and i not in list:
#                 list.append(i)
#     return list
#
# print(common(b,a))
#

# def common(list1,list2):
#     list=[]
#     for i in a:
#         if i in b and i not in list:
#             list.append(i)
#     return list
# print(common(b,a))


#3
# palabras = ['Rober5to','8Andres','J7u7a7n','Al99999den829']
#
# def limpiador(list):
#     nueva=[]
#     cad = ''
#     for i in list:
#         for j in i:
#             if j not in '0123456789':
#                 cad = cad + j
#         nueva.append(cad)
#         cad = ''
#     return nueva
#
# print(limpiador(palabras))





