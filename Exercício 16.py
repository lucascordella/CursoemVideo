#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

from math import trunc
num = float(input('Digite um número: '))
pinteira = trunc(num)
print('O número {} tem como porção inteira {}'.format(num, pinteira))
#print('O número {} tem como porção inteira {}'.format(num, trunc(num)))