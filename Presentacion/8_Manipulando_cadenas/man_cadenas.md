**Manipulando cadenas**  
El texto es una de las formas más comunes de datos que nuestros programas manejarán. En esta parte vamos a mejorar nuestras habilidades en la manipulación de cadenas utilizando métodos de cadena.

przypomnienie(indexowanie,in, not it itd...)  


**Escape characters - caracteres de escape**(escape fuga)
Un carácter de 'escape' le permite utilizar caracteres que, de lo contrario, son imposibles de colocar en una cadena. Un carácter de escape consta de una barra invertida ( *\\* ) seguida del carácter que desea agregar a la cadena.   
Por ejemplo:    
print('El titulo de la pelicula es \'El Rey Leon\' ')

print('Hola!')  
print('\tHola!')

print('Hola!\nQue tal?\nTodo bien?')

**Cadena cruda(raw string)**  
Puede colocar una 'r' antes de la comilla inicial de una cadena para convertirla en una cadena sin formato. Una cadena sin formato omite por completo todos los caracteres de escape y imprime cualquier barra diagonal inversa que aparezca en la cadena.

print('\t Es mi perro,\n se llama Doggy.')
print(r'\t Es mi perro,\n se llama Doggy.')

**Cadenas multilinea(Multiline Strings)**  
Hay una manera más fácil de crear cadenas de varias líneas, sin usar '\n' o '\t'. 
Podemos crear cadenas de esta manera:

print('Hola!\n\nQue tal?')
print('''Hola!

Que tal?''')

**Útiles métodos de cadenas**






The upper(), lower(), isupper(), and islower() String Methods 
The isX String Methods 





