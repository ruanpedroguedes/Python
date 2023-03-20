
"""
Criada pelo(a) prof.
Dissertativa
Faça um programa em Python que utilize todos os comandos de tratamento de erros.

Comandos:

try;

except; 

else 

finally   
"""



try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    result = num1 / num2
except ValueError:
    print("Erro: valor inválido!")
except ZeroDivisionError:
    print("Erro: divisão por zero!")
else:
    print("O resultado da divisão é:", result)
finally:
    print("Programa finalizado!")
