nome =input('Digite seu nome: ')
print(type(nome))
#com 25 espaços
print(f'Prazer {nome:25}!')
#com 25 espaços - alinhado a direita
print(f'Prazer {nome:>25}!')
#com 25 espaços - alinhado a esquerda
print(f'Prazer {nome:<25}!')
#com 25 espaços - alinhado no centro
print(f'Prazer {nome:^25}!')
#com 25 espaços - alinhado no centro preenchendo com algum símbolo
print(f'Prazer {nome:=^25}!')