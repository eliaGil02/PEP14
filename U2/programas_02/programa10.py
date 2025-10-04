"""
Modifica el programa anterior par que pida en primer lugar el número de jugadores que
van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la
banca.
"""

import random

banca = random.randint(17, 21)
numJugadores = int(input("Número de jugadores: "))

for j in range(1, numJugadores + 1):
    print(f"\n--- Jugador {j} ---")
    puntuacion = 0
    while True:
        opcion = input("¿Sacar carta? (si/no): ").strip().lower()
        if opcion == "si":
            carta = random.randint(1, 5)
            puntuacion += carta
            print("Has sacado:", carta, " -  Puntuación:", puntuacion)
            if puntuacion > 21:
                print("Has perdido")
                print("Banca:", banca, " - puntuación:", puntuacion)
                break
        elif opcion == "no":
            if puntuacion > 21:
                print("Has perdido")
            elif puntuacion <= banca:
                print("Puntuación menor o igual que la banca. Has perdido.")
            else:
                print("Puntuación mejor que la banca. Has ganado.")
            print("Banca:", banca, " - puntuación:", puntuacion)
            break

print("\nLa banca tenía:", banca)
