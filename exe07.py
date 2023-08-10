num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 == num2:
    print(f'Os números digitados são iguais!')
elif num1 > num2:
    print(f'O primeiro valor {num1} é maior do que o segundo valor {num2}!')
else:
    print(f'O segundo valor {num2} é maior do que o primeiro valor {num1}!')