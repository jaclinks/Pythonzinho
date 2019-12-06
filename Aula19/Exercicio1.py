# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = [ 'nome',     ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                  'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                  'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                  'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                 ]

# for i in range(0,7):
#     print(f'Nome: {cadastroHBSIS[1][i]} Telefone: {cadastroHBSIS[3][i]} Email: {cadastroHBSIS[5][i]} Idade: {cadastroHBSIS[7][i]}\n')
#     print(f'Nome: {cadastroHBSIS[1][i]} Telefone: {cadastroHBSIS[3][i]} Email: {cadastroHBSIS[5][i]} Idade: {cadastroHBSIS[7][i]}\n')

# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com


# 2 - usando o for, imprima todos nomes um abaixo do outro
# for i in cadastroHBSIS[1]:
#     print(i)
# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)

bibl = []

lista = [1,5,7,3]

for i in range(1,6,2):
    dic = {}
    for j in lista:
        dic[cadastroHBSIS[j - 1]] = cadastroHBSIS[j][i]
    bibl.append(dic)

for i in bibl:
    print(i)

