"""Faça um programa que receba uma frase qualquer, após isso
deve renomear uma palavra dentro da frase e mostrar na tela.
"""

frase = input("Digite uma frase: ")
palavra_antiga = input("Digite a palavra que deseja renomear: ")
palavra_nova = input("Digite a nova palavra: ")

nova_frase = frase.replace(palavra_antiga, palavra_nova)

print("Frase original: ", frase)
print("Frase com a palavra renomeada: ", nova_frase)
