"""
 Utilizando novamente a função range(), mostre os valores com inicio 0, condição de parada em 12, incrementando de 2 em 2.
"""

cont = 0
while cont <= 100:
    print(cont)
    cont += 2
    if cont == 12:
        print('Esse é o número 12')
    continue
    print(cont)