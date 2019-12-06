from CAtv3 import calculaInvestimento

val = float(input('Digite a quantidade de compra: '))

if val == 0:
    print('Valor invalido')
else:
    print(f'O valor total do rendimento sera de {calculaInvestimento(val):.2f}')
