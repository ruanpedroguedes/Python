"""
Desafio: Faça um programa que crie um dicionário e receba do usuário: nome, telefone, endereço e CEP. Lembrando que:

Chaves serão: nome e endereço;

Valores serão: telefone e CEP

Após receber as informações, mostre na tela o dicionário atual, em seguida faça uma condição com verificação para identificar se o nome digitado já existe na lista. Se existir mostre uma mensagem identificando que existe. Se não existir, adicione as informações na lista.
"""


agenda = {}

nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
endereco = input("Digite o endereço: ")
cep = input("Digite o CEP: ")

agenda[nome] = telefone
agenda[endereco] = cep

print("Agenda atual:", agenda)

if nome in agenda:
    print("O nome já existe na lista.")
else:
    agenda[nome] = telefone
    agenda[endereco] = cep
    print("Informações adicionadas à lista.")

print("Agenda atualizada:", agenda)


































"""
dicio = {}
while True:
    for item in range(2):
        nome = input('Informe seu nome: ')
        telefone = int(input('Informe seu telefone: '))
        endereço = input('Informe seu endereço: ')
        cep = int(input('Informe seu cep: '))
       
        if nome in dicio:
            print(print("Já existe essa pessoa", nome))
        else: 
            dicio['nome'] = nome
            print(dicio)
        print(dicio)
"""
    
        