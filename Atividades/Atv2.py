from CAtv2 import rentabilidade, calcula_porcentagem

valorIni  = float(input('Digite o valor inicial para o investimento: '))
taxaJuros = float(input('Taxa de juros: '))

valorCalculo = rentabilidade(valorIni, taxaJuros)

for i in range(1,12):
    valorCalculo = rentabilidade(valorCalculo, taxaJuros) 

print(f'O valor final em R$ é {valorCalculo:.2f}')
print(f'O valor final em % é {calcula_porcentagem(valorIni, valorCalculo):.2f}')
