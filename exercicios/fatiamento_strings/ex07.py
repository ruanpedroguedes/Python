"""
Receba uma frase e faça um verificação usando o in se existe
um nome que você queira descobrir dentro da variável.
"""

frase = input('Informe uma frase: ')
palavra = input('Informe a palavra que deseja encontra na frase: ')

while (palavra in frase) == True:
    print(f'A palavra {palavra}, ESTAR contida na frase {frase}')
    break
else:
    print(f'A palavra {palavra} NÃO estar na frase {frase}')