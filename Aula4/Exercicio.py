n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

lista = [n1, n2, n3, n4]
lista.sort()

'''
if n1 >= n2 and n1 >= n3 and n1 >= n4:
    print(f'{n1} é a maior nota')
elif n2 >= n3 and n2 >= n4:
    print(f'{n2} é a maior nota')
elif n3 >= n4:
    print(f'{n3} é a maior nota')
else:
    print(f'{n4} é a maior nota')

if n1 <= n2 and n1 <= n3 and n1 <= n4:
    print(f'{n1} é a menor nota')
elif n2 <= n3 and n2 <= n4:
    print(f'{n2} é a menor nota')
elif n3 <= n4:
    print(f'{n3} é a menor nota')
else:
    print(f'{n4} é a menor nota')
'''
print(f'A maior nota é {lista[3]}')
print(f'A menor nota é {lista[0]}')

media = (n1 + n2 + n3 + n4) / 4
print(f'A média é {media}')

if media >= 7:
    print('Aprovado')
else:
    print('Reprovado')

