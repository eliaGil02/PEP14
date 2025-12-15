"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
Crea una cadena "Python".
Extrae la subcadena "Pyt" con slicing.
Extrae los caracteres en posiciones pares con slicing ::2.
Invierte la cadena con slicing [::-1].
Recorre la cadena carácter por carácter e imprímelos.
"""

# crear la cadena
cadena = "Python"

# extraer la subcadena "Pyt"
subcadena = cadena[0:3]
print(subcadena)

# extraer caracteres en posicion pares
pares = cadena[::2]
print(pares)

# invertir la cdena
invertida = cadena[::-1]
print(invertida)

# recorrer la cadena caracter a caracter
for caracter in cadena:
    print(caracter)
