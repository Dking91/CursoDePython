a = input ( 'Digite algo: ')

print(' ')

print('O tipo primitivo dessa variavel é: ', type(a))

print(' ')

print('Existem outras possibilidades? ')

print(' ')

print('numerico ', a.isnumeric())
print('alfabeto ', a.isalpha())
print('alfa numerico', a.isalnum())
print('Ascii ', a.isascii())
print('Digito ', a.isdigit())
print('Decimal', a.isdecimal())
print('?',a.isidentifier())
print('minuscula', a.islower())
print('printavel', a.isprintable())
print('espasso', a.isspace())
print('titulo', a.istitle())
print('Maiuscula', a.isupper())
print('Classe/Subclasse', a.__init_subclass__())
