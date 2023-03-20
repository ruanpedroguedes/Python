"""
Faça um programa que receba uma frase, verifique quantas
vezes uma palavra especifica foi repetida dentro dessa frase.
Após isso informe o tamanho da frase.
"""

frase = input('Informe uma frase: ')
palavra = input('Informe a palavra da frase você deseja: ')

contagem = frase.count(palavra)
tamanho = len(frase)

print(f'A palavra: {palavra}, foi repetida {contagem} vezes')
print(f'Essa frase possui {tamanho} caracteres')
