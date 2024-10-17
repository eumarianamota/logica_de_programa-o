#Escreva um programa para ler as coordenadas (X,Y) de uma quantidade indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma).
x = 1
y = 1

while x != 0 or y != 0:
  numbers = input()
  numbers = numbers.split(' ')
  x = int(numbers[0])
  y = int(numbers[-1])
  if x > 0 and y > 0:
    result = 'primeiro'
  elif x < 0 and y > 0:
    result = 'segundo'
  elif x < 0 and y < 0:
    result = 'terceiro'
  elif x > 0 and y < 0:
    result = 'quarto'
  elif x == 0 or y == 0:
    break
  print(result)
