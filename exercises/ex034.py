#Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
v1 = int(input())
v2 = int(input())
v3 = int(input())
v4 = int(input())
v5 = int(input())

pares = 0

if v1 % 2 == 0:
  pares += 1
if v2 % 2 == 0:
  pares += 1 
if v3 % 2 == 0:
  pares += 1
if v4 % 2 == 0:
  pares += 1
if v5 % 2 == 0:
  pares += 1

print(f'{pares} valores pares')