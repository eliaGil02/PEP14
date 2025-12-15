"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Crea una lista de palabras con algunas repetidas.
 Convierte la lista a conjunto para eliminar duplicados.
 Pide al usuario que introduzca una palabra y comprueba si está en el conjunto.
 Muestra el conjunto ordenado de palabras únicas.
"""

# lista con palabras repetidas
palabras = ["hola", "adios", "hola", "python", "adios"]

# convertir la lista en conjunto
conjunto = set(palabras)

print(conjunto)

# pedir una palabra al usuario
palabra = input("Introduce una palabra: ")

# comprobar si está en el conjunto
if palabra in conjunto:
    print("Está en el conjunto")
else:
    print("No está en el conjunto")

# mostrar el conjunto ordenado
print(sorted(conjunto))
