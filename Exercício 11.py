#Crie um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2m².

A = float(input('A altura da parede é: '))
L = float(input('A largura da parede é: '))
Ar = A * L
T = Ar / 2
print('A área da parede é {:.2f}m². \nA quantidade de tinta necessária para sua pintura total é de {:.2f}l.'.format(Ar, T))
