distancia = float(input('Qual a distância seja percorrer em Km: '))

if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45

print(f'O preço da passagem, para distância de {distancia}km, é de R${preco:.2f}!')