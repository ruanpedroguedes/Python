"""
 Agora de forma similiar, crie um dicionário com valores definidos pelo usuário, na tela representar apenas as chaves. Utilize o comando keys().
"""


dados = {}
for item in range(2):
    nome = input('Informe seu nome: ')
    idade = int(input('Informe sua idade: ')) 
    dados[nome] = idade
    
    print(dados.keys())