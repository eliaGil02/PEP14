"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Elimina el cuarto elemento de la lista utilizando la instrucción del.
 Elimina un elemento de la lista utilizando el método remove().
 Verifica si un un elemento pertenece a la lista.
 Muestra por pantalla el índice de un elemento de la lista.
 Muestra por pantalla el número de ocurrencias de un elemento en la lista.
"""

# tupla inicial
tupla = (10, "Python", True, 3.14, 25)

# convertir la tupla a lista
lista = list(tupla)

# eliminar el cuarto elemento
del lista[3]

# eliminar un elemento por valor
lista.remove(True)

# verificar si un elemento pertenece a la lista
print("Python" in lista)

# mostrar indice de un elemento
print(lista.index("Python"))

# mostrar nº de ocurrencias de un elemento
print(lista.count(10))

# convertir en tupla
tupla_final = tuple(lista)
print(tupla_final)
