nome = str(input('Digite o seu nome: '))
nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))

media = (nota1+nota2)/2

if media >= 7:
    print(f'Aluno(a) {nome.capitalize()} teve um bom aproveitamento com média {media:.2f}')
else:
    print(f'Aluno(a) {nome.capitalize()} não teve um bom aproveitamento com média {media:.2f}')