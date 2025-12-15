"""
Escribe un programa en Python que realice las siguientes operaciones con diccionarios.
 Define un diccionario con varias claves y valores.
 Accede a algunos valores usando corchetes [] y muestra los resultados.
 Accede a valores usando get() con y sin valor por defecto.
 Intenta acceder a una clave inexistente con get() y observa el resultado.
"""

# diccionario con datos
persona = {"nombre": "Luis", "edad": 25, "ciudad": "Sevilla"}

# acceso directo a un valor
print(persona["nombre"])

# acceso usando get
print(persona.get("edad"))

# acceso a una clave que no existe
print(persona.get("pais", "No existe"))
