"""
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación
solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va
respondiendo si el número a adivinar es mayor o menor que el introducido. El programa
termina cuando se acierta el número.
Puedes generar el número usando la función random.randrange(1, 21) para
obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio
del programa).
Mejora el programa de forma que el usuario tenga solo 3 intentos.
"""

import random

objetivo = random.randrange(1, 21)
intentos = 3

while intentos > 0:
    n = int(input(f"Adivina el número (1-20). Intentos restantes {intentos}: "))
    if n == objetivo:
        print("Correcto")
        break
    elif n < objetivo:
        print("Mayor")
    else:
        print("Menor")
    intentos -= 1

if intentos == 0 and n != objetivo:
    print("No tienes intentos. El número era:", objetivo)
