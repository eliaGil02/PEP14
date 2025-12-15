"""
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
 Comprueba si ciertas claves existen en el diccionario usando in y not in.
 Muestra el número total de elementos usando len().
 Muestra las claves (keys), los valores (values) y los pares (items).
"""

# diccionario inicial
persona = {"nombre": "Carlos", "edad": 40, "ciudad": "Bilbao"}

# eliminar una clave con del
del persona["ciudad"]

# eliminar una clave con pop y guardar su valor
edad = persona.pop("edad")

print(persona)
print("Edad eliminada:", edad)
