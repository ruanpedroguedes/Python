"""
Faça um programa que receba uma lista de nomes de pessoas e mostre os nomes em maiúsculas. Use o índice para encontrar a string, ou seja, terá que fazer um for e percorrer a lista através da posição e utilize o comando upper() para transformar em maiuscula.
"""

nomes = ['Ruan', 'Ana', 'Carlos', 'Rodrigo', 'Suelen', 'Henrique', 'Bruno']

for i in range(len(nomes)):
    nome = nomes[i]
    nome_maiusculo = nome.upper()
    print(nome_maiusculo)
