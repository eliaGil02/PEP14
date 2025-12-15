"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Crea un conjunto normal y otro inmutable con frozenset().
 Muestra su tipo y contenido.
 Intenta añadir un nuevo elemento al frozenset y observa el resultado.
 Comprueba si el frozenset puede usarse como clave de un diccionario.
"""

# conjunto normal (mutable)
normal = {1, 2, 3}

# conjunto inmutable
inmutable = frozenset({4, 5, 6})

print(type(normal))
print(type(inmutable))

# usar un frozenset como clave de un diccionario
dic = {inmutable: "válido"}
print(dic)
