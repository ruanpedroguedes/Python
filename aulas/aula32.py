"""
Faça um pragrama que peça ao usuário para digitar um número inteiro, informe se este número e par ou impar. Caso o usuário não digite um número interiro, informe que não é um número inteiro
"""

"""entrada = input('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'Impar'
    
    if par_impar is True:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} e {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
"""

"""
Faça um pragrama que pergunte a hora ao usuário e, baseando -se no horário descrito, exiba a saudação apropriada. Ex: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

"""entrada = input('Informe a hora em númros inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >=12 and hora <=17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')

"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""
"""nome = input('Informe seu nome: ')
n_letras = len(nome)

if n_letras > 1 :
    if n_letras <= 4:
        print('Seu nome e curto')
    elif n_letras >= 5 and n_letras <= 6:
        print('Seu nome e normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite pelo menos uma letra.')
"""