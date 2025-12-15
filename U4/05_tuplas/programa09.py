"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Crea una tupla de dos dimensiones que simule una tabla 3x3 de números.
 Recorre todos sus elementos con bucles anidados.
 Crea una tupla que contenga listas como elementos.
 Modifica una de las listas y comprueba si la tupla refleja el cambio.
"""

# tabla bidimensional
tabla = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

# recorrer todo los elementos con bucles anidados
for fila in tabla:
    for elemento in fila:
        print(elemento, end=" ")
    print()


# tupla con listas
tupla_listas = ([10, 20, 30], [40, 50, 60])
# imprimir tupla antes de modificar
print(tupla_listas)

# modificar una de las listas
tupla_listas[0].append(99)
# imprimir tupla despues de modificar
print(tupla_listas)
