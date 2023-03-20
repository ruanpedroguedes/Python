
"""
    1. Faça um programa que receba o nome, idade e a profissão de duas pessoas (utilize a estrutura de repetição for). Após isso, deve armazenar essas informações dentro de uma lista. E mostrar na tela o resultado.

"""
lista = []

for i in range(2):
    nome = input('Informe seu nome: ')
    lista.append(nome)
    idade = int(input('Informe sua idade: '))
    lista.append(idade)
    profissao = input('Informe sua profissão: ')
    lista.append(profissao)
    print(lista)
    break


