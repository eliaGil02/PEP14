"""
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
• La piedra gana a la tijera pero pierde contra el papel.
• El papel gana a la piedra pero pierde contra la tijera.
• La tijera gana al papel pero pierde contra la piedra.
"""

import random

print("Juego: Piedra, Papel o Tijera")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
opcionUsuario = int(input("Seleccione una opción (1, 2 o 3): "))

opcionMaquina = random.randint(1, 3)

opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"}

print("Has elegido:", opciones[opcionUsuario])
print("La máquina eligió:", opciones[opcionMaquina])

if opcionUsuario == opcionMaquina:
    print("Empate")
elif (
    (opcionUsuario == 1 and opcionMaquina == 3)
    or (opcionUsuario == 2 and opcionMaquina == 1)
    or (opcionUsuario == 3 and opcionMaquina == 2)
):
    print("Ganaste")
else:
    print("Perdiste")
