"""
Faça um programa que receba uma frase e depois verifique
se tem a palavra ‘olá’ no início da frase e uma ‘?’ no final da
frase.
"""

frase = input("Digite uma frase: ")



if frase.startswith("olá") and frase.endswith("?"):
    print("A frase começa com 'olá' e termina com '?'")
else:
    print("A frase não atende aos critérios")
