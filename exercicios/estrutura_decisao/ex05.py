"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. 
"""

n1 = float(input('Informe sua nota: '))
n2 = float(input('Informe sua nota: '))
media = (n1+n2)/2

if media >= 9 or media == 10:
    print(f'Média: {media}')
    print(f'Conceito: A')
    print(f'APROVADO')
elif media >= 7.5 or media == 9:
    print(f'Média: {media}')
    print(f'Conceito: B')
    print(f'APROVADO')
elif media >= 6 or media == 7.5:
    print(f'Média: {media}')
    print(f'Conceito: C')
    print(f'APROVADO')
elif media >= 4 or media == 6:
    print(f'Média: {media}')
    print(f'Conceito: D')
    print(f'REPROVADO')
elif media < 4:
    print(f'Média: {media}')
    print(f'Conceito: E')
    print(f'REPROVADO')
else:
    print(f'Valor inválido')