# Aula 20 - 05-12-2019
# Lista com for e metodos

# Com esta lista:
def retornaDic(lista):
    ret = []
    for i in range(1,7):
        dic = {}
        for j in range(0,4):
            dic[lista[0][j]] = lista[i][j]
        ret.append(dic)
    
    return ret

def verificaCod(cod : int, lista):
    ret = retornaDic(lista)
    for i in ret:
        if cod == i['codigo']:
            return True

    return False

def retornaTexto(cod : int , lista):
    ret = retornaDic(lista)

    for i in ret:
        if i['codigo'] == cod:
            print(f"Nome: {i['produto']} , Quantidade: {i['quantidade']} , Valor: {i['valor']}") 

lista = [
         ['codigo','produto','valor','quantidade'],
         [1,'Cevada',15.00,10],
         [2,'Lupulo',150.50,200],
         [3,'Malte',57.80,5000],
         [4,'Levedura 1',10.65,500],
         [5,'Extrato de Levedura',15.00,60],
         [6,'Levedura 2',15.50,87]
        ]

while True:
    cod = int(input('Digite o codigo do produto desejado: '))
    if verificaCod(cod , lista):
        retornaTexto(cod, lista)
    else:
        break

# 2.1 - Faça uma função que pegue esta lista e retorne uma lista com biblioteca.

# 2.2 - Faça outra função para consultar o preço através do código passado
# por parametro. Esta função deve printar o nome do produto, a quantidade
# e o preço.
# Execute esta função dentro do while e quando digitar qualquer código que 
# não tenha produto cadastrado o programa se encerra.
#

