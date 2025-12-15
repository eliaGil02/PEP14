"""
Escribe un programa en Python que realice las siguientes operaciones con listas
partiendo del programa anterior.
 Elimina el cuarto elemento de la lista utilizando la instrucción del.
 Elimina un elemento de la lista utilizando el método remove().
 Verifica si un un elemento pertenece a la lista.
 Muestra por pantalla el índice de un elemento de la lista.
 Muestra por pantalla el número de ocurrencias de un elemento en la lista.
"""

# lista
mi_lista14 = [10, "elemento", "Python", True, 3.14, 25]

# eliminar cuarto elemento con del
del mi_lista14[3]

# eliminar un elemento por valor
mi_lista14.remove("elemento")

# verificar si un elemento pertenece a la lista
print("Python" in mi_lista14)

# mostrar indice de un elemento
print(mi_lista14.index("Python"))

# mostrar ocurrencias de un elemento
print(mi_lista14.count(10))
