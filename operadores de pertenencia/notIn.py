
''' 
Para representar los operadores de pertenencia Python vamos a crear una lista y posteriormente preguntar si un
item a buscar se encuentra dentro de la lista, creamos la variable lista, buscar y result, 
posteriormente vamos a imprimir
'''
lista = [1, 2, 3, 5, 7]

buscar = 4
result = buscar not in lista

print(f'El numero',buscar,"esta en la lista? =", result)