#aalgoritmo para calcular quanto de tinta sera necessario para pintar uma parede

a=float(input('Digite aqui a altura de sua parede: '))
c=float(input('Digite aqui o comprimento de sua parede: '))

m= a * c
t= m/2
print('Com os dados que você nos deu, você tem {} de altura e {} de comprimento.\n{} x {} = {}m²'. format(a,c, a, c, m))
print(' ')
print('Para pintar essa parede você vai precisar de {} litros de tinta'. format(t))
