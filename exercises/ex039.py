#Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:      
#1 x N = N      2 x N = 2N        ...       10 x N = 10N
#A entrada contém um valor inteiro N (2 < N < 1000).

tab = 1
n = int(input())
if 2 < n < 1000:
  while tab <= 10:
    print(f'{tab} x {n} = {tab * n}')
    tab += 1