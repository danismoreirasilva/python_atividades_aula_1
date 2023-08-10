from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Digite o seu ano de nascimento no formato aaaa: '))
idade = anoAtual - anoNasc

if idade >= 18:
    print(f'Você já eleitor, sua idade é de {idade} anos!')
else:
    print(f'Você não é eleitor por ser menor de idade! Sua idade é de {idade} anos!')