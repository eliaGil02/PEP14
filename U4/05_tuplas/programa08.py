"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Crea una cadena de texto con palabras separadas por espacios.
 Divide la cadena en una lista con split() y conviértela a tupla.
 Usa join() para convertir una tupla de palabras en una sola cadena separada por guiones.
 Usa partition() para dividir una expresión y mostrar el resultado como tupla.
"""

# crear cadena de texto
cadena = "Python es un lenguaje de programacion"

# dividir la cadena en lista y convertir a tupla
lista_palabras = cadena.split()
tupla_palabras = tuple(lista_palabras)

print(tupla_palabras)

# convertir tupla a cadena separada por guiones
cadena_guiones = "-".join(tupla_palabras)
print(cadena_guiones)

# partition para dividir una expresion
expresion = "usuario:root"
resultado = expresion.partition(":")
print(resultado)
