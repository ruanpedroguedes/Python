"""
 Faça uma lista set pelo o usuário, recebendo 4 valores e remova um item pelo comando pop() e mostre na tela qual item foi removido. Após isso esvazie a lista e mostre a lista atualizada. 
"""

# Recebe 4 valores do usuário e cria uma lista
valores = []
for i in range(4):
    valor = input("Digite um valor: ")
    valores.append(valor)

# Remove um item da lista usando o comando pop() e mostra na tela qual item foi removido
item_removido = valores.pop()
print("O item removido foi:", item_removido)

# Esvazia a lista e mostra a lista atualizada
valores.clear()
print("A lista atualizada é:", valores)

    

