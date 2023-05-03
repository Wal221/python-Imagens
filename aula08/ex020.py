import random
from random import choice , shuffle

n1 = str(input('Primeiro nome: '))
n2 = str(input('segundo nome: '))
n3 = str(input('terceiro nome: '))
n4 = str(input('quarto nome: '))

lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem da apresentação sera ')
print(lista)

##for listas in lista:
  ##  print(nome)



