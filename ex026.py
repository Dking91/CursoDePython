'''Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

nome = str(input('Digite uma frase no teclado: ')).strip().upper()
print('A letra A aparece {} vezes.'. format(nome.count('A')))
print('A primeira letra A aparece na posição {}.'. format(nome.find('A')+1))
print('A ultima letra A aparece na posição {}.'. format(nome.rfind('A')+1))