"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
from math import prod
numeros = []
while True:
    for i in range(5):
        numero = int(input(f'Informe o {i+1} número inteiro: '))
        numeros.append(numero)
        print(f'Os números digitados foram: {numeros}')

    maior_num = max(numeros)
    menor_num = min(numeros)
    soma_num = sum(numeros)
  

    print(f'Maior número: {maior_num}')
    print(f'Menor número: {menor_num}')
    print(f'Soma dos números: {soma_num}')
    print(f'{prod(numeros)}')
