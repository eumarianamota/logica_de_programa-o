#Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

x = 1
y = 0
while x != y:
  numbers = input()
  numbers = numbers.split(' ')
  x = int(numbers[0])
  y = int(numbers[-1])
  if x < y:
    result = 'Crescente'
  elif x > y:
    result = 'Decrescente'  
  else:
    break
  print(result)  



