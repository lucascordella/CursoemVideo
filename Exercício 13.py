#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salário = float(input('O salário do funcionário é de: R$'))
novo = salário + (salário * 15 / 100)
print('O salário do funcionário com o aumento de 15% é de R${:.2f}.'.format(novo))

