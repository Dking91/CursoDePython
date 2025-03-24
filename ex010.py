#Conversor de moedas

r = float(input('Digite um valor em R$: '))
d = float(5.72)
dc = r / d

print('Você tem R$ {:.2f}\na cotação do dolar esta U$ {:.2f}\nVocê pode comprar m² U${:.2f}'. format(r,d,dc))
