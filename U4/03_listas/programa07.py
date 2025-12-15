"""
Escribe un programa en Python que realice las siguientes operaciones con listas.
 Crea una lista solo de números (ejemplo: temperaturas =).
 Calcula la suma de todos los elementos utilizando la función sum() y la media
(promedio) combinando sum() y len().
 Muestra los valores máximo y mínimo de la lista.
"""

# lista de num
temperaturas = [18, 22, 25, 19, 21, 24]

# suma
suma = sum(temperaturas)
print(suma)

# media
media = suma / len(temperaturas)
print(media)

# max y min
print(max(temperaturas))
print(min(temperaturas))
