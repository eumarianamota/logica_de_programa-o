#Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

n = int(input())
soma = 0

for _ in range(n):
  inteiros = input() #receber dois números inteiros (x e y)
  inteiros = inteiros.split(' ')
  x = int(inteiros[0])
  y = int(inteiros [-1])
  