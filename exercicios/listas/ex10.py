"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
listas = []
pares = []
impar = []
while True:
    for i in range(20): # total de valores
        num = int(input(f'Informe o {i+1} número inteiro: '))
        listas.append(num)
        print(f'Os números digitados foram: {listas}')
    
    for num in listas: # valores pares
        if num % 2 == 0:
            pares.append(num)
    
    for num in listas: # valores impares
        if num % 2 != 0:
            impar.append(num)
    
    print(f'Os números pares São: {pares}')
    print(f'Os números impares São: {impar}')

    

