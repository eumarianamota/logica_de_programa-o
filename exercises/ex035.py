#Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(5):
  number = int(input())

  if number % 2 == 0:
    pares += 1
  else:
    impares += 1

  if number > 0:
    positivos += 1
  elif number < 0:
    negativos += 1

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')
