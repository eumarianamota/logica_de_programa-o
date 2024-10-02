#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
temp_f = float(input('Digite a temperatura em farenheit: '))
temp_c = 5 * (temp_f-32) / 9
print(f'A temperatura em farenheit {temp_f}, convertida para graus celsius é {temp_c}°.')