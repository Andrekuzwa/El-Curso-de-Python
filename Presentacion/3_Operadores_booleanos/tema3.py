#1
num = int(input('Escriba un numero: '))

if num%2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')

#2
edad = int(input('Escriba tu edad: '))

if edad >= 18:
    print('Eres un adulto')
else:
    print('No eres un adulto')

#3
if edad >= 18 and edad % 2 == 0:
    print('Adulto y par')
elif edad >= 18 and edad % 2 !=0:
    print('Adulto y impar')
elif edad < 18 and edad % 2 ==0:
    print('No adulto y par')
else:
    print('No adulto y impar')