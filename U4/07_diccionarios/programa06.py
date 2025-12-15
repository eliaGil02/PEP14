"""
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
 Crea un diccionario con varias claves.
 Elimina una clave con del.
 Elimina otra con pop() y muestra el valor eliminado.
 Usa clear() para vaciar el diccionario.
 Reasigna el diccionario a {} y muestra el resultado.
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
