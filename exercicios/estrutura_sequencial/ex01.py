"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

temperatura = float(input('Informe a temperatura em Fahrenheit:'))

c = 5 * ((temperatura-32) / 9)

print(f'A temperatura em graus celsius e: {temperatura}')