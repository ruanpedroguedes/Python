"""
Faça um programa que leia 2 números pelo teclado e guarde em uma lista. No final mostre quem é o maior e o menor da lista. 
"""

lista = []
n1 = int(input('Infome um número: '))
n2 = int(input('Informe outro número: '))

lista.append(n1)
lista.append(n2)
print(f'Os números inseridos foram {lista}')

if n1 > n2:
    print(f'O número {n1} é maior que {n2} ')

elif n2 > n1:
    print(f'O número {n2} é maior que {n1} ')

else:
    print(f'Os valores {n1} e {n2} são iguais')