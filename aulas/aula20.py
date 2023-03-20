# exercicio



primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

float_valor_1 = float(primeiro_valor)
float_valor_2 = float(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor = {float_valor_1} e maior que o segundo valor = {float_valor_2}')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor = {float_valor_2} e maior que o primeiro valor = {float_valor_1}')
elif primeiro_valor == segundo_valor or segundo_valor == primeiro_valor:
    print(f'O valores {float_valor_1} e {float_valor_2} são iguais')
else:
    print('Digite um valor valido')