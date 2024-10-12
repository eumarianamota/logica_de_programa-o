#Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
kilometers = int(input())
fuel = float(input())

average = kilometers / fuel

print(f'{round(average, 3)} km/l')
