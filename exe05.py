nome = str(input('Digite o seu nome: '))
sexo = str(input('Digite o seu sexo biológico: (F)Feminino ou (M) Masculino: ')).lower()
valor = float(input('Digite o valor das compras: R$ '))


if sexo == 'f':
    print(f'Compras no valor de R${valor:.2f}, tem desconto de R${(13/100)*valor:.2f}')
    print(f'Cliente {nome.capitalize()},o valor a pagar, com desconto, é de R${valor*0.87:.2f}')
elif sexo == 'm':
    print(f'Compras no valor de R${valor:.2f}, tem desconto de R${(5/100)*valor:.2f}')
    print(f'Cliente {nome.capitalize()},o valor a pagar, com desconto, é de R${valor*0.95:.2f}')
else:
    print(f'Não foi digitado uma opção válida para o sexo biológico!')