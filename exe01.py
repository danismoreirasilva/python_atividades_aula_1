vel = int(input('Digite o valor da velocidade em (km/h): '))

if vel > 80:
    excesso = vel-80
    print(f'Você ultrapassou o limite de velocidade!')
    print(f'Velocidade: {vel}km/h, sua multa será de R${excesso*5:.2f}')
else:
    print(f'Não há multas!')