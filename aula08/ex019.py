from random import choice

n1 = str(input('Primeiro nome: '))
n2 = str(input('segundo nome: '))
n3 = str(input('terceiro nome: '))
n4 = str(input('quarto nome: '))

lista = [n1,n2,n3,n4]
nome = choice(lista)

print('O aluno sorteado foi {}'.format(nome))
