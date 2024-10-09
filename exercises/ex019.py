#Faça um Programa que leia três números e mostre-os em ordem decrescente.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

numbers = [n1, n2, n3]

#A função sorted() serve para ordenar uma lista
#O reverse = True ordena uma lista em ordem decrescente 
#O reverse = False ordena uma lista em ordem crescente
sorted_numbers = sorted(numbers, reverse = True) 

print(sorted_numbers)


