import os

def escreve(dado):
    if os.path.exists('ManipulacaoArquivo/Aluno.txt'):
        f = open('ManipulacaoArquivo/Aluno.txt','a')
        f.write(f"{dado['Marca']};{dado['Tipo']};{dado['Teor']}\n")   
        f.close()
    else:
        f = open('ManipulacaoArquivo/Aluno.txt','x')
        f.write(f"{dado['Marca']};{dado['Tipo']};{dado['Teor']}\n")
        f.close()

def le():
    f = open('ManipulacaoArquivo/Aluno.txt','r')
    lista = []
    for i in f:
        linha = i.strip()
        palavras = linha.split(';')
        dado = {'Marca' : palavras[0] , 'Tipo' : palavras[1] , 'Teor' : palavras[2]}
        lista.append(dado)
    f.close()
    return lista

marca = input('Marca: ')
tipo = input('Tipo: ')
teor = float(input('Teor alcoolico: '))

dados = {'Marca' : marca , 'Tipo' : tipo , 'Teor' : teor}
escreve(dados)

for i in le():
    print(f"Nome: {i['Marca']} Tipo: {i['Tipo']} Teor alcoolico: {i['Teor']}")