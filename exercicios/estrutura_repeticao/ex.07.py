"""
Calculadora de duas operações. Faça um programa que receba um menu, nesse menu deverá conter a opção de somar e subtrair. Também deverá criar uma opção de sair do programa. 

Se ele escolher: Somar. Deverá informar dois campos para receber os valores da soma, e o resultado da operação. 

Se escolher: Subtrair. Deverá conter os mesmos dois campos, mas com a operação de subtração.

E se ele escolher sair do programa, deverá interromper o programa

Lembrem-se que a cada laço o ‘sair do programa’ e o menu deverá aparecer. O menu aparecerá no inicio do programa e o sair no fim de cada laço.

RP
Sua resposta
"""
n1 = -1
n2 = -1

while True:
    calcular = input('1 - Para Somar 2 - Para Subtrair e 3 - Para Sair: ')
    if calcular == '1':
        print('Você escolheu SOMA!')
         
        n1 = float(input('Informe uma numero:'))
        n2 = float(input('Informe outro número: '))
        print(f'Soma = {n1 + n2}')
        continue
    
    elif calcular == '2':
        print('Você escolheu SUBTRAÇÃO!')

        n1 = float(input('Informe uma numero:'))
        n2 = float(input('Informe outro número: '))
        print(f'Soma = {n1 - n2}')
        continue
    
    elif calcular == '3':
        print('Você escolheu SAIR do programa')
        continue
    else:
        print('Você digitou um valor INVÁLIDO')
        sair = input('Sair do programa [s]im ou n[ao]: ').lower().startswith('s')
        if sair is True:
            break
        else:
            continue


