#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:

#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

#entrada e cálculo do dinheiro
money_hour = float(input('Quanto você ganha por hora? '))
month_hour = float(input('Quantas horas você trabalha por mês? '))
full_salary = money_hour * month_hour 

#calcular imposto de renda - ir
ir_perc = 0.11 * full_salary
ir = full_salary - ir_perc

#calcular inss 
inss_perc = 0.08 * full_salary 
inss = full_salary - inss_perc

#calcular sindicato 
sind_perc = 0.05 * full_salary
sind = full_salary - sind_perc

#calcular salário líquido 
liquid_salary = full_salary - sind_perc - inss_perc - ir_perc
print(f'Salário bruto: {full_salary} \nIR: {ir_perc} \nINSS: {inss_perc} \nSindicato: {sind_perc} \nSalário Líquido: {liquid_salary}')

