aluno = []

for i in range(0,10):
    temp = [input(f'Digite o nome do aluno {i + 1} : ')]
    for j in range (0,4):
        temp.append(float(input(f'Digite a nota {j + 1} : ')))
    aluno.append(temp)

for i in aluno:
    media = 0
    for j in range(1,5):
        media += i[j]
    media = media / 4
    aprovado = 'Aprovado' if media >= 7 else 'Reprovado'
    print(f'O aluno {i[0]} teve a média {media} e foi {aprovado}')
