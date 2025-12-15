"""
Escribe un programa en Python que escriba tu propia función myslplit(), que se
comporte casi como el método original split(), por ejemplo:
 Debe aceptar únicamente un argumento: una cadena.
 Debe devolver una lista de palabras creadas a partir de la cadena, dividida en los
lugares donde la cadena contiene espacios en blanco.
 Si la cadena está vacía, la función debería devolver una lista vacía.
"""


def mysplit(cadena):
    palabras = []
    actual = ""

    # si la cadena vacia, devolver lista vacia
    if cadena == "":
        return palabras

    for c in cadena:
        if c != " ":
            actual += c
        else:
            if actual != "":
                palabras.append(actual)
                actual = ""

    # añadir la ultima palabra
    if actual != "":
        palabras.append(actual)

    return palabras


# pruebas
print(mysplit("Hola mundo en python"))
print(mysplit("     esto es       una prueba"))
print(mysplit(""))
