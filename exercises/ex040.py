#Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.

n = int(input())
for i in range(n):
  teste = input()
  teste = teste.split(' ')
  x1 = float(teste[0])
  x2 = float(teste[1])
  x3 = float(teste[-1])
  average =  ((x1 * 2) + (x2 * 3) + (x3 * 5))/10
  print(round(average, 1))
