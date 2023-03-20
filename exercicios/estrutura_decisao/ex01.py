"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

pergunta = str(input('Digite  F - Feminino e M - Masculino: '))
m = 'Masculino'
f = 'Feminino'

if pergunta == 'M':
    print(f'Sexo: {m}')
elif pergunta == 'F':
    print(f'Sexo: {f}')
else:
    print('Valor inválido')