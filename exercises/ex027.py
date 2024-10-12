#Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula: 
#Distância: raiz quadrada de (x2 - x1)² + (y2 - y1)²
from math import sqrt
p1 = input()
p2 = input()

#valores de p1
values1 = p1.split(' ')
x1 = float(values1 [0])
y1 = float(values1 [-1])

#valores de p2
values2 = p2.split(' ')
x2 = float(values2 [0])
y2 = float(values2 [-1])

#calcular a distância entre os pontos
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2 )
print(f'{round(distance, 4)}')