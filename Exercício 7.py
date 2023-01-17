#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

A1 = float(input('Primeira nota: '))
A2 = float(input('Segunda nota: '))
print('O aluno tirou {} na primeira prova e {} na segunda prova. \nO resultado de sua média é {}.'.format(A1, A2, ((A1 + A2)/2)))
