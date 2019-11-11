num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))

print('Soma:', num1 + num2)
print('Subtração:', num1 - num2)
print('Multiplicação:', num1 * num2)
print('Divisão:', num1 / num2)

if (num1 > num2):
    print('O primeiro numero é o maior')
elif (num2 > num1):
    print('O segundo numero é o maior')
else:
    print('Os numeros tem o mesmo valor')