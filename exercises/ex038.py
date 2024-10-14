#Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares, de 1 até N, inclusive N, se for o caso.
#A entrada contém um valor inteiro N (5 < N < 2000).

start = 2
n = int(input())
if 5 < n < 2000:
  if n % 2 == 0:

    while start <= n:
      result = start ** 2
      print(f'{start}^2 = {result}')
      start += 2