'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de
um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.'''

from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjassente: '))

#hi = (co **2 + ca ** 2) ** (1/2)
hi = hypot(co,ca)

print('A hipotenusa vai medir {}'.format(hi))