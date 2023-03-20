"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
    salário bruto.
    quanto pagou ao INSS.
    quanto pagou ao sindicato.
    o salário líquido.
    calcule os descontos e o salário líquido, conforme a tabela abaixo:
"""
valor_hora = int(input('Informe o valor ganha por hora:'))

horas_mes = int(input('Informe o valor ganho por mês:')) 

salario = valor_hora*horas_mes

imposto_renda = (salario*11)/100
inss = (salario*8)/100
sindicato = (salario*5)/100

salario_bruto = salario

salario_liquido = salario - imposto_renda - inss - sindicato

print(f'Salário Bruto: {salario_bruto}')
print(f'INSS: {inss}')
print(f'Sindicato: {sindicato}')
print(f'Salário líquido: {salario_liquido}')


