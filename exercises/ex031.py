#Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
#1 - cachorro quente - 4,00
#2 - x salada - 4,50
#3 - x bacon - 5,00
#4 - torrada - 2,00
#5 - refrigerante - 1,50

#definição das variáveis
hotdog = 1
salad = 2
bacon = 3
toast = 4
drink = 5

#recebimento e separação dos valores
product = input()
values = product.split(' ')
type = int(values[0])
amount = int(values[-1])

if type == hotdog: 
  price = amount * 4
elif type == salad: 
  price = amount * 4.50
elif type == bacon:
  price = amount * 5
elif type == toast:
  price = amount * 2
else:
  price =  amount * 1.5

print(f'Total: R$ {price:.2f}')