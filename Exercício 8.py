#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

X = float(input('Digite um valor em metros:'))
print('O valor de {}m em quilômetros é {}. \nO valor de {}m em centímetros é {}. \nO valor de {}m em milímetros é {}.'.format(X, (X/1000), X, (X*100), X, (X*1000)))