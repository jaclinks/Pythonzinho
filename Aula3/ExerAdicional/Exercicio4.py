usuarioPadrao = 'vrau'
senhaPadrao = 'aaaa'

usuario = input('Digite o usuario: ')
senha = input('Digite a senha: ')

if usuario == usuarioPadrao and senha == senhaPadrao:
    print('Bem vindo')
else:
    print('Erro de autenticação')