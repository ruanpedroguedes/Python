"""
Faça um programa que verifique se certo texto está dentro da lista. Mostre na tela através do comando de verificação in.
"""

palavras = ['casa', 'carro', 'avião', 'barco', 'bicicleta']

palavra_procurada = input('Informe a palavra que deseja: ')

if palavra_procurada in palavras:
    print(f'A palavra "{palavra_procurada}" está na lista.')
else:
    print(f'A palavra "{palavra_procurada}" não está na lista.')
