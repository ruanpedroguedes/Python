"""
Peça ao usuário para digitar valores e coloque dentro de um dicionário. Utilize lista e o comando copy() para fazer essa operação. Mostre na tela a lista do tipo list() com as chaves e valores do dicionário.
"""

dicio = dict()
lista = list()

for item in range(2):
    dicio['nome'] = input('nome: ')
    dicio['idade'] = int(input('idade: '))
    lista.append(dicio.copy())

    print(lista)