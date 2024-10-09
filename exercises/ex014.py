#Faça um Programa que peça dois números e imprima o maior deles.
n1 =  float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if n1 > n2:
  result = f'{n1} é maior que {n2}.'
elif n1 < n2:
  result = f'{n2} é maior que {n1}.'
else:
  result = f'{n1} e {n2} são iguais.'

print(result)