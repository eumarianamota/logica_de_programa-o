#Um Posto de combustíveis deseja determinar qual de seus produtos tem a preferência de seus clientes. Escreva um algoritmo para ler o tipo de combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que seja válido). O programa será encerrado quando o código informado for o número 4.


al = 0
gas = 0
di = 0

while True:
  option = int(input())
  if option == 4:
    break

  if option == 1:
    al +=1
  elif option == 2:
    gas += 1
  elif option == 3:
    di += 1

print(f'MUITO OBRIGADO')
print(f'Alcool: {al}')
print(f'Gasolina: {gas}')
print(f'Diesel: {di}')
