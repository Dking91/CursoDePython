'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite some completo: '))
print('Analizando o nome digitado')
print('Nome digitado em maiusculo: {}'. format(nome.upper()))
print('Nome digitado em minusculo: {}'. format(nome.lower()))
