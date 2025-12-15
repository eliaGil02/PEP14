"""
Escribe un programa en Python que realice que extraiga el nombre de usuario y la
contraseña de la siguiente cadena: "usuario:root|contraseña:123456"
"""

# cadena original
cadena = "usuario:root|contraseña:123456"

# separar usuario y contraseña
partes = cadena.split("|")
usuario = partes[0].split(":")[1]
contrasena = partes[1].split(":")[1]

# resultados
print(usuario)
print(contrasena)
