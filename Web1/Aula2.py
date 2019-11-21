from Calculos import divisao_fracionada, divisao_inteira, multiplicacao, raiz, resto_divisao, soma, subtracao

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

print('=' * 50,'\n')

print(f'A soma entre os dois numeros é {soma(n1, n2)}\n')
print(f'A subtração entre os dois numeros é {subtracao(n1, n2)}\n')
print(f'A multiplicação entre os dois numeros é {multiplicacao(n1, n2)}\n')
print(f'A divisão inteira entre os dois numeros é {divisao_inteira(n1, n2):.0f}\n')
print(f'A divisão fracionada entre os dois numeros é {divisao_fracionada(n1, n2)}\n')
print(f'O resto da divisão entre os dois numeros é {resto_divisao(n1, n2)}\n')
print(f'A raiz entre os dois numeros é {raiz(n1, n2)}\n')

print('=' * 50)