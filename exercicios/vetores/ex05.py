"""
Desafio Maroto: Faça uma lista set inicializada manualmente, com tipos de dados: Strings e int. Depois defina opções para o usuário escolher o que ele quer buscar na lista. opção (1) texto, opção (2) inteiros. Quando o usuário escolher a opção, deverá verificar na lista se o valor digitado pelo o usuário está dentro da lista. Se tiver mostrar na tela que existe. Senão, mostrar na tela que não existe. Utilize o comando in para fazer essa verificação. Se o usuário digitar uma opção inválida, deverá fazer o tratamento de erro e mostrar na tela que ele digitou errado. Não é obrigatório o uso de estrutura de repetição, mas é apreciado. J Exemplos de compilação:
"""

lista = ['maçã', 5, 'banana', 10, 'laranja', 15]

opcao = input("O que você quer buscar na lista? Digite '1' para texto ou '2' para inteiros: ")

if opcao == '1':
    texto = input("Digite o texto que você está procurando na lista: ")
    if texto in lista:
        print("O texto", texto, "existe na lista!")
    else:
        print("O texto", texto, "não existe na lista!")
        
elif opcao == '2':
    try:
        numero = int(input("Digite o número inteiro que você está procurando na lista: "))
        if numero in lista:
            print("O número", numero, "existe na lista!")
        else:
            print("O número", numero, "não existe na lista!")
    except ValueError:
        print("Você digitou uma opção inválida!")
        
else:
    print("Você digitou uma opção inválida!")
