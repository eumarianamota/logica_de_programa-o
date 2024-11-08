t = int(input())

n = 0
nn = 0

while n <= 999:
  if n > 1000:
    for i in range(t):
      print(f'N[{nn}] = {i}')
      nn += 1
    break
  n += 1