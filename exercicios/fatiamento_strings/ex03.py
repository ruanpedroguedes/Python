"""
Use os comandos de manipulação de String para verificar se
um dado que o usuário digitar tem apenas letras, ou tem
apenas números, ou então tem letras e números ou se tem
caracteres especiais.
"""

entrada = input('Informe um dado: ')

if (entrada.isalnum() == True):
    print('Os dados tem letras e números')

elif (entrada.isalpha()() == True):
    print('Os dados só possuem letras')

elif (entrada.isnumeric() == True):
    print('Os dados só possuem números ')

else:
    print('Valor inválido')