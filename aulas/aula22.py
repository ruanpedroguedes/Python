# operador lógico or 
# só e necessario um deles ser verdadeiros

entrada = input('[E]entrar [S]sair: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E'or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entra')
else:
    print('Sair')

print(True or False) # Exemplo
