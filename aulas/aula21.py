# Operadores lógicos 
"""
and(e) or(ou) not(não)
"""

# None = não tem valor

entrada = input('[E]entrar [S]sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entra')
else:
    print('Sair')