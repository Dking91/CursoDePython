#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Entre com o valor da temperatura em celsius: '))
f = (9 * c) / 5 + 32
print(' ')
print('A temperatura convertida em graus fahrenheit é: {:.1f}F°'. format(f))
