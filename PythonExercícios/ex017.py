from math import hypot
catoposto = float(input('Comprimento do Cateto Oposto: '))
catadjacente = float(input('Comprimento do Cateto Adjacente: '))
hipotenusa = hypot(catoposto, catadjacente)
print(f'O comprimento da Hipotenusa é {hipotenusa:.2f}')