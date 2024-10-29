#criar uma função para somar dois valores
def add(a, b):
  sum = a + b
  return sum

#executar a função para somar dois valores
x = int(input())
y = int(input())
s = add(x, y)

#exibir o resultado
print(f'A soma de {x} e {y} é igual a {s}.')