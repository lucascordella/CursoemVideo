#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

P1 = float(input('O preço do produto é: R$'))
P2 = P1 - (P1 * 5 / 100)
print('O preço do produto é R${}. \nApós o desconto de 5%, seu novo preço passou a ser R${:.2f}.'.format(P1, P2))