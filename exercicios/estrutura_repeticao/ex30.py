""" 
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
"""

pao = 1
valor_pao = 0.18

while (pao < 51):
    print(f' {pao} - R$: {pao * valor_pao:.2f}')
    pao += 1
    