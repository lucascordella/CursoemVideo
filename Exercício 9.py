#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

X = int(input('Digite um número para abrir sua tabuada: '))
print('{} x {:2} = {} \n{} x {:2} = {} \n{} x {:2} = {} \n{} x {:2} = {} \n{} x {:2} = {} \n{} x {:2} = {} \n{} x {:2} = {} \n{} x {:2} = {} \n{} x {:2} = {} \n{} x {:2} = {}'.format(X, 1, (X*1), X, 2, (X*2), X, 3, (X*3), X, 4, (X*4), X, 5, (X*5), X, 6, (X*6), X, 7, (X*7), X, 8, (X*8), X, 9, (X*9), X, 10, (X*10)))

#Pode ser feito também da seguinte maneira:

Y = int(input('Digite um número para abrir sua tabuada: '))
print('{} x {:2} = {}'.format(Y, 1, Y*1))
print('{} x {:2} = {}'.format(Y, 2, Y*2))
print('{} x {:2} = {}'.format(Y, 3, Y*3))
print('{} x {:2} = {}'.format(Y, 4, Y*4))
print('{} x {:2} = {}'.format(Y, 5, Y*5))
print('{} x {:2} = {}'.format(Y, 6, Y*6))
print('{} x {:2} = {}'.format(Y, 7, Y*7))
print('{} x {:2} = {}'.format(Y, 8, Y*8))
print('{} x {:2} = {}'.format(Y, 9, Y*9))
print('{} x {:2} = {}'.format(Y, 10, Y*10))