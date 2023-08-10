from datetime import date

anoAtual = date.today().year
anoNasc = int(input('Digite o seu ano de nascimento no formato aaaa: '))
idade = anoAtual - anoNasc

if idade < 18:
    print(f'Sua idade atual é {idade} e faltam {18-idade} anos para o seu alistamento!')
else:
    print(f'Sua idade atual é {idade} e  {idade-18} anos já passaram do seu alistamento!')