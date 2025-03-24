#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com N% de aumento ou redução.

s = float(input('Digite aqui o salario do funcionario em R$: '))
p = float(input('Digite aqui o valor da porcentagem: '))
q = input('Digite (a) para aumento ou (r) para redução: ')
print(' ')
au = s + s * p / 100

re = s - s * p / 100
if q == 'a':
    print('O salario do funcionario era R${:.2f}, com o aumento de {}% agora esta R${:.2f}'. format(s, p, au))
elif q == 'r':
    print('O salario do funcionario era R${:.2f}, com a redução de {}% agora esta R${:.2f}'.format(s, p, re))

else:
    print('Você não falou se é um aumento ou redução de salario.')

