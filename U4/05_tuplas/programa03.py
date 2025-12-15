"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Define una tupla de 6 elementos.
 Muestra el primer y último elemento usando índices.
 Muestra una subtupla con los elementos de las posiciones 2 a 4.
 Muestra la tupla en orden inverso.
 Indica cuántos elementos tiene la tupla con len().
"""

# tupla de 6 elementos
tupla = (10, "Python", 3.14, True, "DAW", 25)

# mostrar el primer elemento
print(tupla[0])

# mostrar el ultimo
print(tupla[-1])

# subtupla de posiciones de 2 a 4
subtupla = tupla[2:4]
print(subtupla)

# mostrar tupla en orden inverso
invertida = tupla[::-1]
print(invertida)

# numero de elementos
print(len(tupla))
