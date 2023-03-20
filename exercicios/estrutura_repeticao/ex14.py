"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares pares e a quantidade de números impares
"""

impar = 0
par = 0

for i in range(10):
    if int(input('Informe um número: ')) % 2 == 0:
        par += 1
    else:
        par += 2
    print(f'Número par {par}\nNúmeros impar {impar}')


