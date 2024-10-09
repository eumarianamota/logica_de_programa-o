#Faça um programa que leia cinco valores inteiros, conte quantos desses valores são pares e mostre essa informação.

#Para ler os valores
n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

even = 0 #sempre inicializar uma variável antes de usá-la

#Verificar se é par, se for, adicionar na variável even
if n1 % 2 == 0:
  even += 1 #even = even + 1 só que de forma simplificada
if n2 % 2 == 0:
  even += 1
if n3 % 2 == 0:
  even += 1
if n4 % 2 == 0:
  even += 1
if n5 % 2 == 0:
  even += 1

print(f'{even} valores pares')