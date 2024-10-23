#Beecrowd | 
values = input().split()
a = int(values[0])
n = int(values[1])
soma = 0

if n <= 0:
  n = int(input())

for i in range(n):
  soma += a + i

print(soma)
