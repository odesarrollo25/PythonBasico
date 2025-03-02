'''
Listas, imprimir posicion, validar tamaño, agregar elemento, eliminar elemento, eliminar lista completa
Las listas son muy dinamicas, reciben cualquier tipo de elemento, se pueden adicionar elementos, eliminar, 
vaciar listas, copiar una lista para que no se vea afectada por los cambios, 
concatenar para unir con otras listas y convertir tuplas o conjuntos en listas
'''
lista = [1, 2, 3, 5, 7]

copia = lista.copy()

#Imprimir una posición especifica dentro de la lista
print(f"Posicion 2 =",lista[2])

#Imprimir lista
print(lista)

#Tipo de dato
print(type(lista))

#Tamaño de la lista
print(f"Cantidad de elementos dentro de la lista:",len(lista))

#Adicionar un elemento a la lista
lista.append(9)

#Imprimir lista
print(lista)

#Tamaño de la lista
print(f"Cantidad de elementos dentro de la lista:",len(lista))

#Incertar un elemento a la lista, en una posición especifica
lista.insert(3, 4)

#Imprimir lista
print(lista)

#Tamaño de la lista
print(f"Cantidad de elementos dentro de la lista:",len(lista))

#Adicionar varios elemento a la lista, en una posición especifica
lista.extend([10, 20, 30,40])

#Imprimir lista
print(lista)

#Tamaño de la lista
print(f"Cantidad de elementos dentro de la lista:",len(lista))

#Imprimir lista
print(lista)

#Eliminar elemento
lista.remove(9)

#Tamaño de la lista
print(f"Cantidad de elementos dentro de la lista:",len(lista))

#Imprimir lista
print(lista)

#Eliminar elemento
lista.clear()

#Tamaño de la lista
print(f"Cantidad de elementos dentro de la lista:",len(lista))

#Imprimir lista
print(lista)

#Concatenar 2 listas
lista1=[0, 2, 4, 6, 8]
lista2=[1, 3, 5, 7, 9]

print(lista1+lista2)
print(f"Lista copiada con: lista.copy()",copia)

tuple = 2,4,5
lista3 = list(tuple)
#Tipo de dato
print(type(lista3))

set = {2,4,5}
lista4 = list(set)
#Tipo de dato
print(type(lista4))