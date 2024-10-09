#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
price_one = float(input('digite o valor do produto um: '))
price_two = float(input('digite o valor do produto dois: '))
price_three = float(input('digite o valor do produto três: '))

min = min(price_one, price_two, price_three)

if min == price_one:
  result = f'Você deveria comprar o produto um que custa {min}.'
elif min == price_two:
  result = f'Você deveria comprar o produto dois que custa {min}.'
else:
  result = f'Você deveria comprar o produto três que custa {min}.'

print(result)