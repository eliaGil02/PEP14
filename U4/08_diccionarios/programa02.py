"""
Escribe un programa en Python que cumpla los siguientes requisitos.
 El programa calculará la media de notas de alumnos/as.
 El programa irá pidiendo nombres de alumnos y su calificación
 Los nombres son ingresados en cualquier orden.
 Si un alumno tiene varias notas se pedirá varias veces su nombre y su calificación.
 Cuando se introduzca un nombre vacío se dejaran de pedir datos y se mostrara los
nombre de los alumnos y el promedio de la calificación de cada uno.
Los alumnos se gestionarán con un diccionario (la clave es el nombre) y las calificaciones el valor (que debe ser una tupla).
"""

# diccionario para guardar notas
notas = {}

# pedir datos al usuario
for i in range(3):
    nombre = input("Introduce el nombre del alumno: ")
    nota = float(input("Introduce la nota: "))
    notas[nombre] = nota

# mostrar todas las notas
print(notas)

# calcular la media
suma = 0
for nota in notas.values():
    suma += nota

media = suma / len(notas)

print("Nota media:", media)
