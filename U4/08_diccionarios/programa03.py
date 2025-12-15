"""
Escribe un programa en Python que cumpla los siguientes requisitos.
 Crea un diccionario llamado 'agenda' donde las claves sean nombres de personas y los valores sus números de teléfono.
 Permite añadir, modificar y eliminar contactos.
 Muestra la agenda completa de forma ordenada (por nombre).
 Implementa la búsqueda de un contacto mostrando su número o un mensaje si no
existe.
"""

# diccionario vacío para la agenda
agenda = {}

# añadir algunos contactos
agenda["Ana"] = "600123123"
agenda["Luis"] = "611222333"
agenda["Marta"] = "622333444"

# pedir un nombre al usuario
nombre = input("Introduce un nombre: ")

# comprobar si existe el contacto
if nombre in agenda:
    print("Teléfono:", agenda[nombre])
else:
    print("Contacto no encontrado")

# mostrar todos los contactos
for nombre, telefono in agenda.items():
    print(nombre, "->", telefono)
