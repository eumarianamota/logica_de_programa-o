#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.

#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.

#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

from math import ceil
metros = float(input('Informe, em metros quadrados, o tamanho da área a ser pintada: '))

#calcular a quantidade de latas necessárias
# 1 para 3, assim como 18 para 54
latas = ceil(metros / 54)

#calcular o valor a ser pago 
price = latas * 80

#informa as latas e o valor
print(f'Seram necessárias {latas} latas para pintar a área informada, o valor total dessa quantidade de latas é {price} reais.')

