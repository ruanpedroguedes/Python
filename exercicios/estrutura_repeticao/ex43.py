"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""
total = 0
while True:
    q = int(input('Informe o código: ')) 
    if(q == 999):
        break
    qtd = int(input('Informe a quantidade: '))
    if q == 100:
        total = 1.20 * q 
    elif q == 101:
        total = 1.30 * q
    elif q == 102:
        total = 1.50 * q
    elif q == 103:
        total = 1.20 * q
    elif q == 104:
        total = 1.30 * q
    elif q == 105:
        total = 1 * q
    else:
        print('Código inválido')
    print(f'{total} reias')