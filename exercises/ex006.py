#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo. a soma do triplo do primeiro com o terceiro. o terceiro elevado ao cubo.
num_one = int(input('Digite um número inteiro: '))
num_two = int(input('Digite outro número inteiro: '))
num_real = float(input('Digite um numero real: '))
product = (num_one * 2) * (num_two/2)
sum_one = (num_real * 3) ** 3
print(f'O produto do dobro de {num_one} e metade de {num_two} é {int(product)} e a soma do  triplo de {num_real} elevado ao cubo é {sum_one}.')