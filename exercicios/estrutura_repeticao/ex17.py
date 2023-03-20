"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

num = int(input('Digite o fatorial de um número inteiro: '))

fatorial = 1

while (num > 1):
    fatorial = fatorial * num
    num = num -1
print(f'O fatorial e {fatorial}')