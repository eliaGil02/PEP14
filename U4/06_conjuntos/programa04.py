"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Crea un conjunto con nombres de animales.
 Recorre el conjunto con un bucle for e imprime cada elemento.
 Muestra una lista ordenada de los elementos usando sorted().
"""

# conjunto de animales
animales = {"perro", "gato", "loro", "pez"}

# recorrer el conjunto
for animal in animales:
    print(animal)

# mostrar el conjunto ordenado
print(sorted(animales))
