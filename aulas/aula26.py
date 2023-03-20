"""
Formatação básica de strings

s - strings
d - int
float - float

> - Esquerda
< - Direita
^ - Centro
= - força o número a aparecer antes dos zeros
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') # preenche em espaços
print(f'{variavel: >10}') # preenche em espaços
print(f'{variavel:0^10}') # preenche com 0, o que você quiser

print(f'{10000.56748393847565784:0=+10,.1f}')
print('O hexadecimal de 1500  é {1500:08X}')

print(f'{variavel!r}')