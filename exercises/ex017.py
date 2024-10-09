#Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite outro número: '))

max = max(n1, n2, n3)
min = min(n1, n2, n3)

if min == max:
  result = 'Todos os números são iguais.'
else:
  result = f'O maior número é o {max} e o menor é o {min}.'

print(result)
