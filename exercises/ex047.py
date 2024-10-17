#Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao impossivel” para os valores em questão.
times = int(input())
for _ in range(times):
  numbers = input()
  numbers = numbers.split(' ')
  x = float(numbers[0])
  y = float(numbers[-1])
  if y == 0:
    print('divisao impossivel')
  else:
    division = x / y
    print(division)
