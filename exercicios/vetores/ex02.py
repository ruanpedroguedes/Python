"""
Faça um programa que receba pelo o usuário 5 nomes de pessoas e seus respectivos estados, utilize a estrutura de repetição for retornando os dados dentro de uma lista set. E depois verifique se foi retornado na class set.  
"""

listaSet = set()
for i in range(5): # Adicionando na lista
    nome = input(f'Informe o {i+1} nome:  ')
    estado = input(f'Informe o {i+1} estado: ')
    listaSet.add(nome)
    listaSet.add(estado)
    print(f'Os nomes adicionados foram: {nome}')
    print(f'Os estados adicionados foram: {estado}')

# verificação 

for i in listaSet:
    nome = input('Qual nome deseja encontrar: ')
    if nome not in listaSet:
        print(f'{nome} NÃO estar na lista')
    else:
        print(f'{nome} ESTAR na lista')
    estado = input('Qual estado deseja encontrar: ')
    if estado not in listaSet:
        print(f'{estado} NÃO estar na lista')
    else:
        print(f'{estado} ESTAR na lista')
    break
    
