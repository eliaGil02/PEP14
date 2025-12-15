"""
Basándote en los programas anteriores, crea:
 Clase Manada con:
◦ Atributos de instancia: lista_animales.
◦ Constructor __init__(self, lista_animales)
◦ Métodos añadir(animal).
◦ Implementa iter() y next() para iterar la manada animal por animal.
 Crea una función main que:
◦ Cree una manada.
◦ Añada tres animales (de cualquier tipo)
◦ Recorra la manada con un for.
"""


# Clase que será usada por otra
class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def mostrar_info(self):
        print(f"Motor de {self.potencia} CV")


# Clase que contiene un Motor (composición)
class Coche:
    def __init__(self, marca, potencia_motor):
        self.marca = marca
        self.motor = Motor(potencia_motor)

    def mostrar_info(self):
        print(f"Coche marca {self.marca}")
        self.motor.mostrar_info()


# Programa principal
def main():
    coche1 = Coche("Toyota", 120)
    coche2 = Coche("Seat", 90)

    coche1.mostrar_info()
    coche2.mostrar_info()


main()
