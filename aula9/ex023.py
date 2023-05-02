from shlex import join

number = input('Digite um numero ')
print(number.split())
#print(' '.join(number).split(','))

dividido = number.split()
print('O', dividido[0][0], 'e as centenas')
print('O', dividido[0][1], 'e as dezenas')
print('E o ', dividido[0][2], 'as unidades')