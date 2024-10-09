#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

shift = input('Sendo as letras \n\nM - manhã \nV - vespertino \nN - noturno \n\nDigite o turno em que você estuda: ').upper()

if shift == 'M':
  result = 'Bom dia!'
elif shift == 'V':
  result = 'Boa tarde!'
elif shift == 'N':
  result = 'Boa noite!'
else: 
  result = 'Valor inválido.'

print(result)