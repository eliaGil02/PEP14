"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Crea una tupla con varios valores repetidos.
 Busca el índice de un elemento usando index().
 Muestra cuántas veces aparece un elemento usando count().
 Comprueba si un valor está en la tupla (in) o no está (not in).
"""

# crear una tupla con valores repetidos
tupla = (10, "Python", 3.14, "Python", 10, "Java", 10)

# buscar el indice de un elemento
indice = tupla.index("Python")
print("Indice de Python: ", indice)

# cuantas veces aparece un elemento
print(tupla.count(10))

# si un valor esta en la tupla
print("Java" in tupla)

# si un valor no esta en la tupla
print("C++" not in tupla)
