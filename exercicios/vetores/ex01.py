"""
Faça um programa que declare um set manualmente, deve receber nome, idade e sexo. Após isso, mostre na tela o resultado. 
"""

listaSet = set()
for i in range(3):
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: '))
    sexo = input('Informe seu sexo [m/f]: ').lower()
    listaSet.add(nome)
    listaSet.add(idade)
    listaSet.add(sexo)
    print(listaSet)