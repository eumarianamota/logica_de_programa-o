#Criando uma calculadora

def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mul(x, y):
  x * y

def div(x, y):
  x // y

line = input()
oper1, oper2, operation = line.split()

oper1 = int(oper1)
oper2 = int(oper2)

if operation == '+':
  result = add(oper1, oper2)
elif operation == '-':
  result = sub(oper1, oper2)
elif operation == 'x':
  result = mul(oper1, oper2)
else:
  result = div(oper1, oper2)

print(f'{oper1} {operation} {oper2} = {result}') 