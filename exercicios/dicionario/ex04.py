"""
Faça um dicionário definido com valores inteiros, depois faça uma verificação dentro desse dicionário se um valor (específico) está dentro dessa lista. Utilize o comando in para fazer essa verificação.
"""

valores = {'n1': 12,
           'n2': 1000,
        'n3': 3000
}


while True:
    valor = int(input('Digite um número inteiro que deseja encontrar: '))
    if valor in valores.values(): 
        print(f'O valor {valor} ESTAR DENTRO')
    else:
        print('O valor NÃO estar dentro')
            