#Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

number = int(input()) #recebe o número
if number % 2 == 0:   #verifica se ele é par
  number += 1         #se ele for par, torna-o ímpar

for i in range(6):    #para i em uma sequência de 6, faça:
  print(number)       #printar o number
  number += 2         #criar um novo number + 2

#dessa forma, você recebe um número e consegue tirar todos os seis números ímpares consecutivos de forma simplificada com o for.
