nome = input(('Informe seu nome:'))
idade = int(input('Informe sua idade: '))
nome_invertido = (nome[::-1])
n_letras = len(nome)

if nome and idade:
    print(f'Seu nome e: {nome}')
    print(f'Seu nome invertido e {nome_invertido}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')
    
    print(f'Seu nome contém {n_letras} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e : {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')