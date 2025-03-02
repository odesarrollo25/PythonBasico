'''
Las tuplas, a diferencia de las listas, son inmutables, no se pueden modificar depues de crearlas
las tuplas se pueden definir con () o simplemente separadas por comas (,)
en ellas es posible imprimir posicion, validar tamaño, Las tuplas son muy dinamicas, 
reciben cualquier tipo de elemento, se pueden adicionar elementos por medio de la concatenación
'''
tupla = (1, 2, 3, "Hola")
print(tupla)
print(len(tupla))

lista = [1, 2, 3, 5, 7]
tuple1 = tuple(lista)
print(type(tuple1))

conjunto = {1, 2.5, "Hola", False}
tuple2 = tuple(conjunto)
print(type(tuple2))
print(tuple2)
print(tuple2[2])
concatenar =(tupla+tuple2)
print(len(concatenar))
print(concatenar)