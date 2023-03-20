"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A 
"""
gabarito = ['A', 'B', 'C', 'D', 'E', 'E', 'D', 'C', 'B', 'A'] #gabarito da prova
total_alunos = 0
soma_notas = 0
maior_acerto = 0
menor_acerto = 10

while True: 
    respostas = []
    for i in range(10):
        resposta = input(f'Informe a {i+1} questão: ')
        respostas.append(resposta.upper())
    
    acertos = 0
    for i in range(10):
        if respostas[i] == gabarito[i]:
            acertos += 1

    nota = acertos
    soma_notas += nota
    total_alunos += 1

    if acertos > maior_acerto:
        maior_acerto = acertos

    if acertos < menor_acerto:
        menor_acerto = acertos

    print(f'Números de acertos: {acertos}')
    print(f'Nota {nota}')

    opcao = input(f'Outro aluno vai utilizar o sistema ? (S/N)' )
    if opcao.upper() == 'N':
     break

    media_notas = soma_notas / total_alunos
    print(f'Maior acerto: {maior_acerto}')
    print(f'Menor acerto: {menor_acerto}')
    print(f'Total de alunos que utilizaram o sistema: ')
    print(f'Médias das notas dos alunos: {media_notas:.2f}')