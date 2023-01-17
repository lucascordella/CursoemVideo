#AULA 07
nome = input('Qual é o seu nome?')
print('Prazer em te conhecer{}!'.format(nome))

#Caso eu queira deixar o nome aparecer em 20 caracteres vou utilizar {:20}
#Para colocar alinhamentos: {:>20} o alinhamento fica a direita. Alinhado a esquerda: {:<20}
#Para centralizar nesses 20 espaços: {:^20}
#Para colocar = em volta nesses 20 espaços e centralizado: {:=^20}

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

#Caso eu queira deixar a divisão em apenas 3 casas flutuantes, eu coloco: {:.3f}
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))

#Caso eu queira deixar tudo na mesma linha sem quebrar, eu coloco no final após o () do format: ,end=' ')
print('A soma é {}, o produto é {} e a divisão é {}'.format(s,m,d),end=' >>> ')
print('Divisão inteira {} e potência {}'.format(di, e))

#Para quebrar a linha (ir para uma nova linha), eu coloco: \n. Ex: 'A soma é {}, \n o produto é {}'
print('A soma é {}, \n o produto é {}, \n e a divisão é {}'.format(s,m,d))
