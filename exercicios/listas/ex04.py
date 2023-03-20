"""
    4. Faça um programa que receba 10 números e depois coloque em ordem crescente e decrescente. Use e o comando sort() e sort(reverse = True).

"""

numero = [1,5,6,44,33,77,465,54,43,23]

numero.sort()
print(f'Números em ordem crescente\n{numero}')

numero.sort(reverse=True)
print(f'Números em ordem descrescente\n{numero}')