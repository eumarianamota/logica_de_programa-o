#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
#area = pi * r²
from math import pi
raio = float(input('Digite o valor do raio: '))
area = pi * raio**2
print(f'A área do círculo é {area}.')