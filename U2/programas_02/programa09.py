"""
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer
lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A
continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando
para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la
banca gana.
"""

import random

banca = random.randint(17, 21)
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
