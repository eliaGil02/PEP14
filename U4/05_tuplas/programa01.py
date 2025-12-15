"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Crea varias tuplas con diferentes tipos de datos (int, float, str, bool).
 Crea una tupla vacía y otra con un solo elemento (usa la coma final).
 Crea una tupla sin paréntesis.
 Muestra el tipo de cada tupla usando type()
"""

# tuplas con diferentes tipos de datos
tupla1 = (10, 3.14, "Python", True)
tupla2 = (1, 2.5, "Hola", False)

# tupla vacia
tupla_vacia = ()

# tupla solo un elemento
tupla_elemento = (5,)

# tupla sin parentesis
tupla_sin_parentesis = 7, 8.5, "Tupla", True

# mostrar tipo de cada tupla
print(type(tupla1))
print(type(tupla2))
print(type(tupla_vacia))
print(type(tupla_elemento))
print(type(tupla_sin_parentesis))
