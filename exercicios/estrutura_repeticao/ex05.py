"""
 Faça um programa que leia um nome de usuário e a sua senha. Não aceite a senha igual ao nome do usuário, caso isso ocorra, deve mostrar uma mensagem de erro e voltar a pedir as informações.
"""


while True:
    nome = input('Informe seu nome: ')
    senha = input('Informe sua senha: ')

    if senha == nome:
        print('[ERRO], senha deve ser diferente de nome')
        break
    else:
        print('Acesso AUTORIZADO')