"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Usa comprensión de conjuntos para crear:
◦ Un conjunto con los números del 1 al 10.
◦ Un conjunto con los cuadrados de los números del 1 al 10.
◦ Un conjunto con los números pares del 1 al 20.
 Muestra los resultado
"""

# crear un conjunto con números del 1 al 10
a = {i for i in range(1, 11)}

# crear un conjunto con cuadrados
b = {i**2 for i in range(1, 11)}

# crear un conjunto con números pares
c = {i for i in range(1, 21) if i % 2 == 0}

print(a)
print(b)
print(c)