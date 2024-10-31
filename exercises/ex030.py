#Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

seconds = int(input())

#calcular horas
hours = seconds // 3600
hours_rest = seconds % 3600

#calular minutos
minutes = hours_rest // 60
minutes_rest = seconds % 60

#calcular segundos
seconds = minutes_rest

#resultado 
print(f'{hours}:{minutes}:{seconds}') 