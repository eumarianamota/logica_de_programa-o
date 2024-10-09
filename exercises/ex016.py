#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar: A mensagem "Aprovado", se a média alcançada for maior ou igual a sete; A mensagem "Reprovado", se a média for menor do que sete; A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

average = (n1 + n2) / 2

if 10 > average >= 7:
  result = 'Aprovado'
elif average == 10:
  result = 'Aprovado com Distinção'
else:
  result = 'Reprovado'

print(result)
