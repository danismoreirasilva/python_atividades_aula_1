larg = float(input('Digite a largura do terreno: '))
comp = float(input('Digite o comprimento do terreno: '))

area = larg * comp

if area < 100:
    print(f'Área: {area:.2f}m² - Terreno Popular!')
elif area < 500:
    print(f'Área: {area:.2f}m² - Terreno Master!')
else:
    print(f'Área: {area:.2f}m² - Terreno VIP!')