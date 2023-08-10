nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if media <= 4.9:
    print(f'A média {media:.2f}: Reprovado!')
elif media <= 6.9:
    print(f'A média {media:.2f}: Em recuperação!')
else:
    print(f'A média {media:.2f}: Aprovado!')