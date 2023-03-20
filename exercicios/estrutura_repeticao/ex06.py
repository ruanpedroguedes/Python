"""
  Faça um programa que receba as seguintes informações do usuário: Nome, idade e salário. Valide as seguintes informações:

O nome deve ser maior que 3 caracteres, ou seja, o nome Ana, por exemplo, não passaria no laço de repetição. Dica: use o método len() para verificar o tamanho do nome. 

Idade deve estar entre 0 e 150. 

O salário não pode ser negativo.

O programa só retornará os dados finais se todos os critérios forem atendidos, caso algum critério não passar, deve continuar o loop até o usuário acertar.

Dica: Use o laço de repetição while, três vezes, um para cada validação. 
"""

nome = ""
idade = -1
salario = -1

while len(nome) <= 3:
    nome = input('Informe seu nome (Maior que 3 caracteres): ')

while idade < 0 or idade > 150:
    idade = int(input('Informe sua idade: '))
    
    if idade < 0 or idade > 150:
        print('Idade INVÁLIDA') 

while salario < 0:
    salario = float(input('Informe seu sálario: '))
    
    if salario < 0:
        print('Sálario INVÁLIDO')

print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Sálario {salario}')




