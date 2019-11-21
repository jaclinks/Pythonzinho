lista_jogador = []

for i in range(0,12):
    dicionario = {
        'Nome'     : input(f'Digite o nome do jogador {i + 1}: '),
        'Posicao'  : input(f'Digite a posicao: '),
        'Numero'   : input(f'Digite o numero da camisa: '),
        'PernaBoa' : input(f'Qual a perna boa: ')
    }
    lista_jogador.append(dicionario)

for i in lista_jogador:
    for x,y in i.items():
        print(x, '-', y)