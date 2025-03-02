'''
Los set o conjuntos, a diferencia de las listas, son inmutables reciben cualquier tipo de elemento, 
se pueden adicionar elementos utilizando la union, en ellos es posible imprimir posicion, validar tamaño.
'''

lista = [1, 2, 3, 5, 7]
conjunto1 = set(lista)
print(type(conjunto1))

copia = conjunto1.copy()

print(f"Copia de conjunto1",copia)

tuple = 2,4,5
conjunto2 = set(tuple)
#Tipo de dato
print(type(conjunto2))

#Union
concatenar = (conjunto1 | conjunto2)
print(concatenar)

#Intersección
concatenar = (conjunto1 & conjunto2)
print(concatenar)