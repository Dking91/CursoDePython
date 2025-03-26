'''Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''

'''Não foi necessario importar uma biblioteco pois é possivel usar a conversão de variavel int'''
#from math import trunc

num = float(input('Digite um valor: '))
print(' O valor digitado foi {} e a sua porção é {}'.format(num, int(num)))