"""
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
 Crea dos diccionarios con algunas claves comunes.
 Combínalos en un nuevo diccionario usando el operador |.
 Actualiza uno de ellos con update().
 Crea una copia con copy() y muestra los identificadores (id()) para comprobar
que son distintos.
"""

# diccionario original
original = {"a": 1, "b": 2}

# copia del diccionario
copia = original.copy()

# mostrar identificadores
print(id(original))
print(id(copia))

# modificar la copia
copia["c"] = 3

print("Original:", original)
print("Copia:", copia)
