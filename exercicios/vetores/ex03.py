"""
 Faça uma lista set já inicializada com valores strings, após isso, deverá pedir para o usuário adicionar um nome que deseja adicionar a lista e outro nome que deseja remover da lista.  
"""
listaSet = {'ruan','pedro', 'felipe', 'caio', 'gustavo', 'gomes'}
for i in range(1):
    user_adicionar = input('Informe um nome para adicionar na lista: ')
    listaSet.add(user_adicionar)
    print(f'O nome adicionado foi {user_adicionar}')
    user_remove = input('Informe um nome da lista para remover: ')
    listaSet.remove(user_remove)
    print(f'O nome removido foi {user_remove}')
    print(listaSet)
