
# i=0
# for letra in 'palabra':
#     print(letra,i)
#     i += 1

# print('Que gol!')
# for i in range(5):
#     print('Gol!')

# print('Que gol!')
# i = 0
# while i < 5:
#     print('Gol!')
#     i += 1


# for i in range(5):
#     print('FUERA - ' + str(i))
#     for j in range(2):
#         print('Iteración del bucle DENTRO - ' + str(j))


# 1
# num = int(input('Cuanto numeros?'))
# for i in range(num):
#     print(i)
#
# num = int(input('Cuanto numeros?'))
# i=0
# while i < num:
#     print(i)
#     i+=1


# 2
# for i in range(10):
#     for j in range(10):
#         if i % 2 != 0:
#             if j%2 == 0 :
#                 print('+ ', end='')
#             else:
#                 print('- ', end='')
#         else:
#             if j%2 == 0 :
#                 print('- ', end='')
#             else:
#                 print('+ ', end='')
#     print()

3
frase = input('Escriba una frase: ')
for i in range(len(frase)-1, -1, -1):
    print(frase[i], end='')

frase = input('Escriba una frase: ')
s1 = ''
for i in frase:
    s1 = i + s1
print(s1)
