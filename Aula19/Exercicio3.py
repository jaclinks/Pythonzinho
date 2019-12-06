# Aula 19 - 04-12-2019
# Lista com for e metodos

# Como comer um gigante.... é com um pedaço de cada vez.
# Na hora de fazer este exercicio, atentar para 

# Com o arquivo de cadastro.txt onde possui os seguintes dados: codigo cliente, nome, idade, sexo, e-mail e telefone
# 1 - Crie um metodo que gere e retorne uma lista com bibliotecas com os dados dos clientes
# 2 - Com a lista do exercicio 1, separe os adultos dos menores de idade e salve em um arquivo .txt cada.
# Esta função tambem retornar uma lista com a biblioteca dos maiores de idades.
# 3 - Crie uma função que conte quantas mulheres e quantos homens tem na lista. Salve cada um em um arquivo diferente.
# 4 - Faça uma função de consulta de cadastro. A função deve receber o valor do código do cliente e deve imprimir na 
# tela os dados do cliente com f-string usando a lista do exercicio 1
#  4.1 - A pesquisa deve aparecer uma frase para as seguintes condições:
#           Mulheres até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!""
#           Mulheres acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor alegria! O seu 
#                                            cruch vai adorar!"
#           Mulheres acima de 18:  "Olá {nome}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico
#                                                com o dobro de sabor!!!"
#           Homens até 16 anos: "Ola {nome}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!""
#           Homens acima de 16 a 18 anos: "Olá {nome}! Quer experimentar nosso refigerante sabor Corriga de carros!  
#                                          A sua amada vai adorar!"
#           Homens acima de 18:  "Olá {nome}! Já experimentou nossa cerveja? alto teor alcoolico
#                                                com o dobro do amargor!!!"
#      Lembre-se: É importante que apareça a frase. Pois a mesma será encaminhada por e-mail pela equipe de marketing

def retornaPessoas(d):
    f = open('Aula19/Cadastro.txt','r')
    ret = []
    for j in f:
        sep = j.strip().split(';')
        dic = {}
        for i in range(0,6):
            dic[d[i]] = sep[i]
        ret.append(dic)
    f.close()
    
    return ret 

def separa(d):
    lista = retornaPessoas(d)
    maior = []
    menor = []

    for i in lista:
        if int(i['idade']) < 18:
            menor.append(i)
        else:
            maior.append(i)
    
    f = open('Aula19/Maiores.txt','a')

    for i in maior:
        s = ''
        for j in range(0,6):
            if j > 0:
                s += f';{i[d[j]]}'
            else:
                s += f'{i[d[j]]}'
        s += '\n'
        f.write(s)
    f.close()

    a = open('Aula19/Menores.txt','a')
    for i in menor:
        s = ''
        for j in  range(0,6):
            if j > 0:
                s += f';{i[d[j]]}'
            else:
                s += f'{i[d[j]]}'
        s += '\n'
        a.write(s)
    a.close()

    return maior

def separaHM(d):
    lista = retornaPessoas(d)

    h = []
    m = []

    for i in lista:
        if i['sexo'] == 'm':
            h.append(i)
        else:
            h.append(i)
    
    f = open('Aula19/Homem.txt','a')

    for i in h:
        s = ''
        for j in range(0,6):
            if j > 0:
                s += f';{i[d[j]]}'
            else:
                s += f'{i[d[j]]}'
        s += '\n'
        f.write(s)
    f.close()

    f = open('Aula19/Muier.txt','a')
    for i in m:
        s = ''
        for j in range(0,6):
            if j > 0:
                s += f';{i[d[j]]}'
            else:
                s += f'{i[d[j]]}'
        s += '\n'
        f.write(s)
    f.close()

def consulta(d):
    lista = retornaPessoas(d)

    cod = input('Digite o codigo da pessoa: ')

    for i in lista:
        if i['CodCli'] == cod:
            for j,k in i.items():
                print(f'{j} : {k}')

def mensagem(d):
    lista = retornaPessoas(d)

    for i in lista:
        if i['sexo'] == 'f':
            if int(i['idade']) < 16:
                print(f"Ola {i['nome']}! Você quer aproveitar nosso Tikito sabor Gloss? É uma delicia!")
            elif int(i['idade']) <= 18 :
                print(f"Olá {i['nome']}! Quer experimentar nosso refigerante sabor alegria! O seu cruch vai adorar!")
            else:
                print(f"Olá {i['nome']}! Já experimentou nossa bebida a base de tequila? Baixo tero alcoolico com o dobro de sabor!!!")
        else:
            if int(i['idade']) < 16:
                print(f"Ola {i['nome']}! Você quer aproveitar nosso Tikito sabor Meleka? É uma delicia!")
            elif int(i['idade']) <= 18 :
                print(f"Olá {i['nome']}! Quer experimentar nosso refigerante sabor Corriga de carros! A sua amada vai adorar!")
            else:
                print(f"Olá {i['nome']}! Já experimentou nossa cerveja? alto teor alcoolico com o dobro do amargor!!!")

d = ['CodCli','nome','idade','sexo','email','telefone']
separa(d)
separaHM(d)
consulta(d)
mensagem(d)