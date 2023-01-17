#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians
ang = float(input('Escreva um valor: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O valor do ângulo é {:.2f}, seu seno vale {:.2f}, seu cosseno vale {:.2} e sua tangente vale {:.2f}.'.format(ang, sen, coss, tang))
