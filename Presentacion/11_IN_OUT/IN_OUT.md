**Leyendo y escribiendo archivos**
1.dwa rodzaje plikow b i string
2.(ściezka)open i rodzaje otwierania
3.czytanie
4.wpisywanie i dodawanie
5.indeks


To open a file we can use open() funcion which returns file object. Two first esential parameters are filepath and access mode.  
If the file is in working directory we can pass name of the file as a string.  
file = open('ejemplo.txt')

If the file resides in a directory other than that, you have to provide the full path with the file name.

file = open('C:\\\Users\\\Andre\\\Curso\\\IN_OUT')  

We can open a with a diffrent access mode depending on our intentions. Firstly we can open it as a binary file or text file but today we are going to talk about text part.

Secondly depends what do want to do with a file read, write or append text.








