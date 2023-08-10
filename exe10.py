nome = str(input('Digite o nome do funcionário: ')).title()
salario = float(input('Digite o salário: R$ '))
tempoServico = int(input('Quantos anos trabalha na empresa: '))

if tempoServico <= 3:
    salario *= 1.03
elif tempoServico <= 10:
    salario *= 1.125
else:
    salario *= 1.2

print(f'Funcionário: {nome} terá novo salário de: R$ {salario:.2f}! ')