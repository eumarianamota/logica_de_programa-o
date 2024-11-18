#Beecrowd | 1021

value = float(input())

#valores das notas
values_notes = []
notes = [100, 50, 20, 10, 5, 2]

for note in notes:
  values_notes.append(value // note)
  value = value % note

#valores das moedas
values_coins = []
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

for coin in coins:
  values_coins.append(value // coin)
  value = value % coin

values_coins = [int(coin) for coin in values_coins]
values_notes = [int(note) for note in values_notes]

print('NOTAS:')
print(f'{values_notes[0]} nota(s) de R$ 100.00')
print(f'{values_notes[1]} nota(s) de R$ 50.00')
print(f'{values_notes[2]} nota(s) de R$ 20.00')
print(f'{values_notes[3]} nota(s) de R$ 10.00')
print(f'{values_notes[4]} nota(s) de R$ 5.00')
print(f'{values_notes[5]} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{values_coins[0]} moeda(s) de R$ 1.00')
print(f'{values_coins[1]} moeda(s) de R$ 0.50')
print(f'{values_coins[2]} moeda(s) de R$ 0.25')
print(f'{values_coins[3]} moeda(s) de R$ 0.10')
print(f'{values_coins[4]} moeda(s) de R$ 0.05')
print(f'{values_coins[5]} moeda(s) de R$ 0.01')