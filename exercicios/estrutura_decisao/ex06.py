"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

"""

combustivel = input('Informe A - Álcool G - Gasolina: ')
litros = int(input('Quantos litros você deseja: '))

preco_gasolina = 2.50
preco_alcool = 1.90

ate_20_alcool = (litros * preco_alcool) * 0.03
acima_20_alcool = (litros * preco_alcool) * 0.05
ate_20_gasolina = (litros * preco_gasolina) * 0.04
acima_20_gasolina = (litros * preco_gasolina) * 0.06

if combustivel == 'A' or combustivel == 'a': # alcool 
    print('Você escolheu Álcool')

    if litros < 20:
        print(f'Valor a pagar: {(preco_alcool * litros)}')
        print(f'Valor do desconto: {ate_20_alcool}')
        print(f'Valor a pagar pós desconto: {(preco_alcool*litros) - (ate_20_alcool)}')

    if litros >= 20:
        print(f'Valor a pagar: {preco_alcool * litros}')
        print(f'Valor do desconto: {acima_20_alcool}')
        print(f'Valor a pagar pós desconto: {(preco_alcool*litros) - (acima_20_alcool)}')

elif combustivel == 'G'or combustivel == 'g': # Gasolina
    print(f'Você escolheu Gasolina')

    if litros < 20:
        print(f'Valor a pagar: {(preco_gasolina*litros)}')
        print(f'Valor do desconto: {(ate_20_gasolina)}')
        print(f'Valor a pagar pós desconto: {(preco_gasolina*litros) - (ate_20_gasolina)}')
    
    if litros >= 20:
        print(f'Valor a pagar: {(preco_gasolina*litros)}')
        print(f'Valor do desconto: {acima_20_gasolina}')
        print(f'Valor a pagar pós desconto: {(preco_gasolina*litros) - (acima_20_gasolina)}')
else:
    print('Valor inválido')