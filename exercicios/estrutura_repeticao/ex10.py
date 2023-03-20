"""
Faça um programa que receba dois valores inteiros e gere os números inteiros que estão no intervalo compreendido por eles
"""

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe outro número inteiro: '))


while n2 < n1:
    n1 = int(input('Informe um número inteiro: '))
    n2 = int(input('Informe outro número inteiro: '))

else:
        for i in range(n1,n2,1):
         print(i)