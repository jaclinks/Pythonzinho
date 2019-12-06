# Aula 20 - 05-12-2019


# Surgiu a necessidade de envio massivo de e-mails dos clientes cadastrados
# no arquivo cadastro1.txt 

# >>>> Fazer tudo com metodos <<<<<

# 1 - Para isso o programa necessita que separe os clientes maiores de 20 anos 
# em um arquivo separado chamado menores_de_idade.txt

# 2 - Separar os clientes femininos e salvar em um arquivo chamado feminini.txt

# 3 - Fazer um terminal de consulta onde se digita o código cliente e 
# imprima na tela o (f-string) o codigo, nome, idade, sexo, email, telefone.
# Se digitar um número que não exista, deverá aparecer uma mensagem dizendo
# "código não encontrado!" Se digitar 'S' (sair) o programa deve finalizar.

def lerPessoas():
    f = open('Aula20/cadastro.txt','r',encoding='utf8')
    d = ['codigo','nome','idade','sexo','email','telefone']

    r = []

    for i in f:
        dic = {}
        s = i.strip().split(';')
        for j in range(0,6):
            dic[d[j]] = s[j]
        r.append(dic)

    f.close()
    return r

def separaMaior():
    lista = lerPessoas()
    d = ['codigo','nome','idade','sexo','email','telefone']
    g = []

    for i in lista:
        if int(i['idade']) >= 20:
            g.append(i)
    
    f = open('Aula20/maior_de_idade.txt','a')

    for i in g:
        s = ''
        for j in range(0,6):
            if j > 0:
                s += f';{i[d[j]]}'
            else:
                s += f'{i[d[j]]}'
        s += '\n'
        f.write(s)
    
    f.close()

def separaMulher():
    lista = lerPessoas()
    d = ['codigo','nome','idade','sexo','email','telefone']
    g = []

    for i in lista:
        if i['sexo'] == 'f':
            g.append(i)

    f = open('Aula20/mulher.txt','a')

    for i in g:
        s = ''
        for j in range(0,6):
            if j > 0:
                s += f';{i[d[j]]}'
            else:
                s += f'{i[d[j]]}'
        s += '\n'
        f.write(s)
    
    f.close()
    
#separaMaior()
#separaMulher()

def retornaPessoa(lista, codigo):
    for i in lista:
        if i['codigo'] == codigo:
            return f"codigo: {i['codigo']}, Nome: {i['nome']}, Idade: {i['idade']}, Sexo: {i['sexo']}, Email: {i['email']}, Telefone: {i['telefone']}"
    return 'Pessoa nao encontrada'

r = ''
lista = lerPessoas()
while r != 's':
    cod = input('Digite o codigo da pessoa desejada: ')
    print(retornaPessoa(lista, cod))
    r = input('Deseja terminar? ')

