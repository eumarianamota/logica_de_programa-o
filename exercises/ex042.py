i = 1
j = 8
while i <= 9: #enquanto i for menos ou igual a 9
  for _ in range(3): #cria um for para repetir um range de 3
    j -= 1
    print(f'I={i} J={j}')
  i += 2
  j = 8