"""
Escribe un programa en Python que realice las siguientes operaciones con tuplas.
 Crea una tupla con tres valores y asígnalos a tres variables mediante desempaquetado.
 Usa el operador * para desempaquetado extendido.
 Define una función media(*args) que calcule la media de varios números y
pruébala con diferentes argumentos.
"""

# tupla con 3 valores
tupla = (10, 20, 30)

# desempaquetar en 3 variables
a, b, c = tupla
print(a, b, c)

# desempaquetado extendido
tupla2 = (1, 2, 3, 4, 5)

x, *resto, y = tupla2
print(x)
print(resto)
print(y)


# funcion media con *args
def media(*args):
    resultado = 0

    if len(args) != 0:
        resultado = sum(args) / len(args)

    return resultado


# pruebas
print(media(10, 20, 30))
print(media(5, 15))
print(media(1, 2, 3, 4, 5))
