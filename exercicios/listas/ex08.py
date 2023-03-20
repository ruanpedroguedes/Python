"""Faça um programa que receba uma tupla e realize a adição de um elemento fazendo a conversão. Mostre na tela a lista e a tupla modificada.
"""

tupla = (45,56,89,89,44)

valor = input('Informe um valor para adicionar a tupla: ')

if valor.isdigit():
    valor = int(valor)

elif "." in valor:
    valor = float(valor)

lista = list(tupla)
lista.append(valor)

tupla_modificada = tuple(lista)

print(f'Lista modificada {lista}')
print(f'Tupla modificada: {tupla_modificada}')
  