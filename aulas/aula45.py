"""
Iterável = str, range, etc (__iter__)
Iterador = quem sabe entregar um valor por vez
next = me entregue o proximo valor
iter = me entregue seu iterador
"""
"""texto = iter('Luiz')  #.__iter__()

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
"""

texto = 'Luiz'


"""while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break
"""

for letra in texto:
    print(letra)
