#Leia um valor inteiro N, entre 2 e 1000 (2 < N < 1000) e mostre a tabuada de N.
n = int(input())
tab = 1
if 2 < n < 1000:
  while tab <= 10:
    print(f'{n} x {tab} = {n * tab}')
    tab += 1
