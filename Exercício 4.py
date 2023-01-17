#Desafio da aula 6: Faça um programa que leia alggo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
L = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(L)))
print('Só tem espaços? {}'.format(L.isspace()))
print('Está tudo em letra maiúscula? {}'.format(L.isupper()))
print('Só tem número? {}'.format(L.isnumeric()))
print('Só tem letra? {}'.format(L.isalpha()))