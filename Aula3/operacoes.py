nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))

print(f'Nome: {nome} Sobrenome: {sobrenome} Idade: {idade}')

if idade < 18:
    print('Menor que 18')
else:
    print('Maior igual 18')

if 5 > 2:
    print("Five is greater than two!")