"""
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
 Crea un diccionario 'persona' que contenga otro diccionario 'direccion' como valor.
 Accede a un elemento del diccionario anidado (por ejemplo, número de la calle).
 Crea un diccionario 'familia' con varios miembros (cada uno con sus propios datos).
 Muestra los datos de cada miembro recorriendo el diccionario.
"""

# diccionario vacío para la agenda
agenda = {}

# añadir contactos
agenda["Ana"] = "600123123"
agenda["Luis"] = "611222333"

# pedir un nombre al usuario
nombre = input("Introduce un nombre: ")

# comprobar si existe en la agenda
if nombre in agenda:
    print("Teléfono:", agenda[nombre])
else:
    print("Contacto no encontrado")
