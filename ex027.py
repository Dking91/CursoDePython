'''Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente.'''

nome = str(input('Digite nome completo: ')).strip()

sepnome = nome.split()

print('O primeiro nome digitado é {}.'.format(sepnome[0]))
print('O ultimo nome digitado é {}.'. format(sepnome[-1]))