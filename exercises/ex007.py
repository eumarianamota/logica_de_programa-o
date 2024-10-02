#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.

#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.

#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.

#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input('Quantos quilos de peixe você pescou? '))
if peso > 50:
  more = peso - 50
  multa = more * 4
  print(f'Você pescou {peso}kg, logo, foram {more}kg a mais, então você deverá pagar {multa} reais pelo excesso.')
else:
  print(f'Você pescou {peso}kg, então não deverá pagar multa.')