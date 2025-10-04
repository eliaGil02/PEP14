"""
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que
saque mayor puntuación total, gana. Si la puntuación total coincide, gana quien haya
sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
Puedes pedir el valor de cada tirada de dados por teclado o usar la la función
random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
debes poner import random al inicio del programa)
"""

import random

dado1J1 = random.randrange(1, 7)
dado2J1 = random.randrange(1, 7)
dado1J2 = random.randrange(1, 7)
dado2J2 = random.randrange(1, 7)

totalJ1 = dado1J1 + dado2J1
totalJ2 = dado1J2 + dado2J2

print("Jugador 1 -", dado1J1, "y", dado2J1, "=", totalJ1)
print("Jugador 2 -", dado1J2, "y", dado2J2, "=", totalJ2)

if totalJ1 > totalJ2:
    print("Gana el Jugador 1")
elif totalJ2 > totalJ1:
    print("Gana el Jugador 2")
else:
    maxJ1 = max(dado1J1, dado2J1)
    maxJ2 = max(dado1J2, dado2J2)
    if maxJ1 > maxJ2:
        print("Gana el Jugador 1 (por dado más alto)")
    elif maxJ2 > maxJ1:
        print("Gana el Jugador 2 (por dado más alto)")
    else:
        print("Empate")
