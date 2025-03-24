#fazer um conversor de medidas
m =float(input("Digite uma medida em metro: "))
dm = m * 10
cm = m * 100
mm = m * 1000
da = m / 10
hm = m / 100
km = m / 1000

print("O valor que você digitou foi {}.". format(m))
print(' ')
print('Valor digitado em KM: {}\nValor digitaado em Hm: {}\nValor digitado em dam: {}\nValor digitado em dm: {}\nValor digitado em cm: {}\nValor digitado em mm: {}'. format(km, hm,da,dm,cm,mm))