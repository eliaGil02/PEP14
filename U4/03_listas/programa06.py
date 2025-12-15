"""
Escribe un programa en Python que realice las siguientes operaciones con listas:
 Crea un cadena de caracteres con varias palabras y a partir de ella crear una lista
que contenga como elementos las palabras de la cadena.
◦ Usa la método split().
◦ Usa método partition()
 Crea lista que contenga como elementos varias palabras y partir de ella crear una
cadena de caracteres que contenga las palabras separadas por guiones.
"""

# cadena original
cadena = "Hola buenos dias"

# lista usando split
lista_split = cadena.split()
print(lista_split)

# lista usando partition
antes, sep, dsps = cadena.partition(" ")
lista_partition = [antes] + dsps.split()
print(lista_partition)


# lista de palabras
lista_palabras = ["HOLA", "QUE", "TAL", "ESTAS"]

# crear cadena con guiones
cadena_guiones = "-".join(lista_palabras)
print(cadena_guiones)
