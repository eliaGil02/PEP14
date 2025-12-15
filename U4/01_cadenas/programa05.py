"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
Declara dos cadenas y únelas con concatenación (+).
Repite una cadena tres veces con *.
Compara dos cadenas lexicográficamente e indica cuál es mayor.
Comprueba si una subcadena pertenece a otra con in.
"""

# declaracion de dos cadenas
cadena1 = "Hola"
cadena2 = "Mundo"

cadena_unida = cadena1 + " " + cadena2
print(cadena_unida)

# repetir una cadena 3 veces
cadena_repetida = cadena1 * 3
print(cadena_repetida)

# comparacion lexicografica de cadenas
if cadena1 > cadena2:
    print(f'"{cadena1}" es mayor que "{cadena2}"')
elif cadena1 < cadena2:
    print(f'"{cadena2}" es mayor que "{cadena1}"')
else:
    print("ambas cadenas son iguales")

# comprobar si una subcadena pertenece a otra
subcadena = "la"

if subcadena in cadena1:
    print(f'La subcadena "{subcadena}" está dentro de "{cadena1}"')
else:
    print(f'La subcadena "{subcadena}" no está dentro de "{cadena1}"')
