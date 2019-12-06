# Aula 19 - 04-12-2019
# Lista com for e metodos

cab = ['nome', 'telefone', 'email','idade']

pess   = [  
            ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
            ['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
            ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
            ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]   
        ]

# 1 - Usando estas 2 listas, fazer uma função que crie retorne uma lista com dicionários
# com os dados das pessoas com idade maior ou igua a 18 anos
def Q1():
    retorno = []
    for i in range (0,7):
        dic = {}
        for j in range (0,4):
            dic[cab[j]] = pess[j][i]

        if int(dic['idade']) >= 18:
            retorno.append(dic)

    return retorno
#  2 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (não prescisa usar o f-string, .format())

for i in Q1():
    print(i)
#  3 - Imprima a lista resultante com um for imprimindo um dicionário em cada linha 
# (usando o f-string)
for i in Q1():
    for j,k in i.items():
        print(f'{j} : {k}') 
    print('\n')