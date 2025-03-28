'''Faça um programa que leia um número de 0 a 9999 e mostre na
tela cada um dos dígitos separados'''

num = int(input('Digite um numemero inteiro: '))
#n = str(num)
'''print('Analizando o numero {} .'. format(num))
print('unidade: {}'. format(n[3]))
print('dezena: {}'. format(n[2]))
print('centena: {}'. format(n[1]))
print('milhar: {}'. format(n[0]))'''

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10




print('Analizando o numero {} .'. format(num))
print('unidade: {}'. format(u))
print('dezena: {}'. format(d))
print('centena: {}'. format(c))
print('milhar: {}'. format(m))
