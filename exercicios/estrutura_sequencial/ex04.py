"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

tamanho_metros = float(input('Informe o tamanho em metros quadrados: '))

litros = tamanho_metros / 6
latas = litros / 18

if latas % 18 != 0:
    latas += 1  

    preco = latas * 80

    galoes = litros / 3.6

elif galoes % 3.6 != 0:
    galoes += 1 

    valor_galao = galoes * 25

# mistura entre latas e galões

mistura_latas = int(litros / 18.0)
mistura_galao = int((litros - (mistura_latas * 18)) / 3.6)

if litros - (mistura_latas * 18) % 3.6 != 0:
    mistura_galao += 1

print(f'Apenas latas de 18L {latas} preço: {preco}')

print(f'Apenas galoes de 3.6 litros: {galoes} preço {valor_galao}')

print(f'Mistura de latas:{mistura_latas} Mistura galao:{mistura_galao}')



