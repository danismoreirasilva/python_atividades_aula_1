a = int(input('Digite o valor lado A: '))
b = int(input('Digite o valor lado B: '))
c = int(input('Digite o valor lado C: '))

eh_triangulo =  a < b+c and b < a+c and c < a+b

if eh_triangulo:
    if a == b and b == c:
        print(f'É um triangulo Equilátero')
    elif a != b and a != c and b != c:
        print(f'É um triangulo Escaleno')
    else:
        print(f'É um triangulo Isósceles')

else:
    print(f'Não é triangulo')
