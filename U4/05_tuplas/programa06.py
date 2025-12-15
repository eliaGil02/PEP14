"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Crea dos tuplas con valores distintos y únelas con +.
 Repite una tupla dos veces con *.
 Asigna la tupla a una nueva variable (copia = tupla) y muestra sus identificadores
con id().
 Comprueba si ambas variables apuntan al mismo objeto.
"""

# crear las tuplas
tupla1 = (1, 2, 3)
tupla2 = ("Python", "Java")

# unir las tuplas
tupla_unida = tupla1 + tupla2
print(tupla_unida)

# repettir tupla dos veces
tupla_repetida = tupla1 * 2
print(tupla_repetida)

# asignar la tupla a otra variable
copia = tupla1

# mostrar id de memoria
print(id(tupla1))
print(id(copia))

# apuntan al mismo ojeto
print(tupla1 is copia)
