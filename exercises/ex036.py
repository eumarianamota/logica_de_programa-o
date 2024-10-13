#Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

number = int(input())
number_abs = abs(number)
rep = 1

while rep <= 6:
  if number_abs % 2 == 0:
    number += 1
    print(number)
  else: 
    number += 2
    print(number)
  rep += 1

