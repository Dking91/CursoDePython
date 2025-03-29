'''Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.'''

nomec = str(input("Digite nome completo: ")).strip()


print('O nome digitado tem Silva ? {}'. format('silva' in nomec.lower()))