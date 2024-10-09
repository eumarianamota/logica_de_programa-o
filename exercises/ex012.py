#Leia um valor inteiro x, apresente 6 valores ímpares consecutivos, inclusive o x se for o caso, um por linha.
n = int(input())
if n % 2 == 0:
  n += 1

count = 0
while count < 6:
  print(n)
  n += 2
  count += 1