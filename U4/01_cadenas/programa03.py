"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
Declara variables con tu nombre, curso y año.
Muestra un mensaje con str.format().
Muestra el mismo mensaje usando f-strings.
Usa un f-string para mostrar el resultado de una operación matemática con dos
números.
"""

# declaracion de variables
nombre = "Elia"
curso = "DAW"
anno = 2025

# mensaje usando str.format
mensaje = "Mi nombre es {}, estudio {} y estamos en el año {}.".format(
    nombre, curso, anno
)
print(mensaje)

# mensaje usando f-strings
mensaje2 = f"Mi nombre es {nombre}, estudio {curso} y estamos en el {anno}."
print(mensaje2)

# operacion matematica
num1 = 8
num2 = 4
resultado = num1 + num2
print(f"La suma de {num1}+{num2} es {resultado}.")
