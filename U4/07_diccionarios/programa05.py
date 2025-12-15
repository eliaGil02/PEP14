"""
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
 Crea un diccionario con varios pares clave-valor.
 Recorre las claves con un bucle for.
 Recorre los valores con un bucle for.
 Recorre las claves y valores a la vez usando items().
"""

# diccionario de un alumno
alumno = {"nombre": "Laura", "nota": 8, "curso": "DAW"}

# recorrer usando las claves
for clave in alumno:
    print(clave, alumno[clave])

print("-----")

# recorrer usando items()
for clave, valor in alumno.items():
    print(clave, ":", valor)
