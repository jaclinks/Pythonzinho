import os

def escrever():
    if not os.path.isdir('/Dados'): 
        os.mkdir('Dados')
    
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')

    arquivo = nome + ',' + idade + '\n'

    if os.path.exists('Dados/Aluno.txt'):
        f = open('Dados/Aluno.txt','a')
        f.write(arquivo)   
        f.close()
    else:
        f = open('Dados/Aluno.txt','x')
        f.write(arquivo)   
        f.close()

def ler_tudo():
    f = open('Dados/Aluno.txt', 'r')

    listaArquivo = []

    for x in f:
        listaArquivo.append(x)

    listaSeparada = []

    for x in listaArquivo:
        listaSeparada.append(x.split(','))

    for x in listaSeparada:
        print(f'Nome: {x[0]}')
        print(f'Idade: {x[1]}')

    f.close()

def mostra_menu():
    print('=' * 20)
    print('Digite 1 para cadastrar')
    print('Digite 2 para ler tudo')
    print('Digite 3 para sair')
    print('=' * 20)

mostra_menu()
escolha = input('Digite sua escolha: ')

while escolha != '3':
    if escolha == '1':
        escrever()
    else:
        ler_tudo()

    mostra_menu()
    escolha = input('Digite sua escolha: ')
