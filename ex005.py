#Digitar um numero, mostrar ele na tela e apresentar seu antecessor e sucessor.

n = int(input('Digite um numero: '))
print('Você digitou {}, o numero antes dele é {} e o numero depois dele é {}'.format(n, n-1, n+1))
#Poderia usar mais de uma variavel caso fosse necessario essa informação mais a frente no codigo, mas como não foi, usei somente uma variavel.