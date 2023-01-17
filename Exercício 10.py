#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

D = float(input('Sua carteira possui a quantia total de reais: R$'))
DD = D / 5.10
print('Você pode comprar US${:.2f} com o dinheiro guardado em sua carteira.'.format(DD))