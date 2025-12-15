"""
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
 Crea una cadena o lista y genera un diccionario que cuente la frecuencia de cada elemento usando compresión.
 Crea otro diccionario que asigne números del 1 al 5 con sus cuadrados.
 Muestra ambos resultados.
"""

# diccionario con otros diccionarios dentro
alumnos = {
    "alumno1": {"nombre": "Ana", "nota": 7},
    "alumno2": {"nombre": "Luis", "nota": 9},
}

# acceder a datos anidados
print(alumnos["alumno1"]["nombre"])
print(alumnos["alumno2"]["nota"])
