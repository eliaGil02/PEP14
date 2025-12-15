"""
Escribe un programa en Python que realice las siguientes operaciones con listas.
 Crea una lista que contenga 30 veces la palabra “Vacío”
 Crear una lista que contenga los 10 primeros números pares.
"""

# lista vacio
lista_vacio = ["Vacío"] * 30
print(lista_vacio)

# lista pares
pares = []

for i in range(1, 11):
    pares.append(i * 2)
print(pares)
