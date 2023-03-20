"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo: 
"""

while True:
    total = 0
    print("========== LOJA DO SR. MANOEL JOAQUIM ==========")
    while True:
        preco = float(input('Informe o valor do produto que deseja[Ou digite o número 0 para sair] : '))
        if preco == 0:
            break
        total += preco
        print(f'O total das compras é {total:.2f} reais')
        valor = float(input('Quanto foi pago no  total das compras: '))
        troco = valor - total
        print(f'Troco {troco}')
        
        
            
       

