"""
Faça um programa que peça uma nota, entre zero e dez. Se o usuário digitar uma nota menor que zero ou maior que dez, deverá mostrar uma mensagem de erro, e pedir novamente a nota. Quando o usuário colocar uma nota válida, deverá mostrar o valor na tela e parar o loop.
"""


while True:
    nota = -1
    nota = float(input('Informe sua nota (entre 0 e 10): '))
    if nota < 0 or nota > 10:
        print('[ERRO], Digite uma nota entre 0 e 10')
        break 
    else:
        print(f'{nota} é uma nota válida')
