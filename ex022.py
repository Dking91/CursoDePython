'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite some completo: ')).strip()
print('Analizando o nome digitado')
print('Nome digitado em maiusculo: {}'. format(nome.upper()))
print('Nome digitado em minusculo: {}'. format(nome.lower()))
print('Nome digitado em title: {}'. format(nome.title()))

print('O nome digitado tem ao todos {} letras.'. format(len(nome) - nome.count(' ')))

#print('Seu primeiro nome tem  {} letras'. format(nome.find(' ')))

separa =nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
print('Seu segundo nome é {} e ele tem {} letras.'.format(separa[1], len(separa[1])))