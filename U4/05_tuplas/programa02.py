"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Crea una lista de f juegos y conviértela a tupla usando tuple().
 Convierte nuevamente la tupla a lista.
 Muestra los tipos antes y después de cada conversión.
"""

# lista de juegos
juegos = ["FIFA", "Minecraft", "Zelda", "Mario", "Tetris"]

# mostrar tipo
print(type(juegos))

# convertir a tupla
juegos_tupla = tuple(juegos)
print(type(juegos_tupla))

# convertir a lista again
juegos_lista = list(juegos_tupla)
print(type(juegos_lista))
