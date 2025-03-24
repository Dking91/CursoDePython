#criando um algoritimo para calcular a porcentagem

valor = float(input('Digite aqui o valor do protudo que você quer calcular: '))
porcentagem = float(input('Digite aqui o valor da porcentagem: '))

#desconto = valor - valor * porcentagem  100
vdesconto= valor * porcentagem / 100
desconto = valor - valor / 100 * porcentagem
print('Seu produto custa R$ {}, com o desconto de {}% ele passa a custar R${}'. format(valor, porcentagem, desconto))
print('O desconto foi de R$ {}'. format(vdesconto))
