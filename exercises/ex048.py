#Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

m1 = float(input())
while m1 < 0 or m1 > 10:
  print('nota invalida') 
  m1 = float(input())

m2 = float(input())
while m2 < 0 or m2 > 10:
  print('nota invalida') 
  m2 = float(input())

average = (m1 + m2) / 2
print(f'media = {average}')