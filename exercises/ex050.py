#Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.
n1 = int(input())
n2 = int(input())
soma = 0
if n1 < n2:
  for _ in range(n1, n2 + 1): 
    if _ % 13 != 0:
      soma += _
else:
  for _ in range(n2, n1 + 1): 
    if _ % 13 != 0:
      soma += _
print(soma)