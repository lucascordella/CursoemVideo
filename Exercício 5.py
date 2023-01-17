#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input('Digite um número'))
a = n1 - 1
s = n1 + 1
print('O antecessor de {} é {} e o sucessor de {} é {}'.format(n1, a, n1, s))

#Para fazer sem outras variáveis, no lugar de a e s no format coloca: (n-1) e (n+1)
