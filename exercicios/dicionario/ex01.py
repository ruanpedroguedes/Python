"""
Crie um dicionário recebendo dados pelo usuário, após isso deve retornar apenas os valores do dicionário. Utilize o comando values() para fazer esse retorno.
"""

dados = {}
for item in range(2):
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: ')) 
    dados[nome] = idade
    
    print(dados.values())