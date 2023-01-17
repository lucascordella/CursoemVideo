#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
cat1 = float(input('O comprimento do cateto oposto é: '))
cat2 = float(input('O comprimento do cateto adjacente é: '))
hip = math.sqrt(cat1**2 + cat2**2)
#hip = (cat1**2 + cat2**2) ** (1/2)
print('O cateto oposto vale {}, o cateto adjacente vale {}. O valor da hipotenusa desse triângulo é {:.2f}.'.format(cat1, cat2, hip))