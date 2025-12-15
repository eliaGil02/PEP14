"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Crea un conjunto con varios números enteros.
 Crea otro conjunto con cadenas de texto.
 Crea un conjunto vacío con set() y muestra su tipo.
 Comprueba que los conjuntos no permiten elementos duplicados.
"""

# crear un conjunto con números (no admite duplicados)
numeros = {1, 2, 3, 3, 4}

# crear un conjunto con cadenas
colores = {"rojo", "verde", "azul", "rojo"}

# crear un conjunto vacío
vacio = set()

# mostrar los conjuntos
print(numeros)
print(colores)
print(vacio)

# mostrar el tipo de dato
print(type(vacio))
