"""
Faça um programa que leia 5 números e informe a soma e a média dos números
"""
lista = []

for i in range(5):
    n1 = int(input(f'Digite o {i+1}º número: '))
    lista.append(n1)
    n2 = int(input(f'Digite o {i+2}º número: '))
    lista.append(n2)
    n3 = int(input(f'Digite o {i+3}º número: '))
    lista.append(n3)
    n4 = int(input(f'Digite o {i+4}º número: '))
    lista.append(n4)
    n5 = int(input(f'Digite o {i+5}º número: '))
    lista.append(n5)
  
    soma = n1 + n2 + n3 + n4 + n5
    media = (n1 + n2 + n3 + n4 + n5) / 5


    print(f'Os valores informados foram {lista}')
    print(f'Soma: {soma}')
    print(f'Média: {media}')






    