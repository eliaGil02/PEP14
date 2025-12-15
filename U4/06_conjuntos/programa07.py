"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Crea un conjunto con varios colores.
 Crea una copia con copy() y verifica que tienen distintos identificadores usando
id().
 Usa update() para añadir todos los elementos de otro conjunto.
 Muestra ambos conjuntos antes y después de la actualización.
"""

# conjunto original
colores = {"rojo", "verde", "azul"}

# copia del conjunto
copia = colores.copy()

# mostrar identificadores
print(id(colores))
print(id(copia))

# actualizar el conjunto original
otros = {"amarillo", "negro"}
colores.update(otros)

print(colores)
print(copia)