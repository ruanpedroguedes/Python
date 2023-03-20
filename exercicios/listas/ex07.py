"""
Faça um programa que receba uma lista com 10 valores inteiros e guarde em uma lista. Após isso, armazene em outra lista apenas com números pares. Mostre na tela a nova lista com os valores recebidos.
"""

valores = []

for i in range(10):
    valor = int(input(f'Digite o {i+1}º valor: '))
    valores.append(valores)
    print(valores)

pares = []
for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)

# mostra na tela a nova lista com os valores pares
print(f'Os valores pares digitados foram: {pares}')