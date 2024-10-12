#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input('Digite uma número inteiro entre zero e dez: '))

if 10 >= nota > 0:
  print(nota)
else: 
  print('valor inválido!') 
  nota = int(input('Digite uma número inteiro entre zero e dez: '))
