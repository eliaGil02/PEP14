"""
Amplia el programa anterior para que la función main:
 Cree una lista con varios objetos Mamifero y Ave.
 Recorra la lista y llame a saluda por cada objeto.
"""


# Clase base
class AnimalTerrestre:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    def saluda(self):
        print(f"Soy un animal terrestre llamado {self.nombre}")


# Subclase Mamifero
class Mamifero(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.gestacion_dias = gestacion_dias

    def saluda(self):
        print(
            f"Soy un mamífero llamado {self.nombre} "
            f"y mi gestación dura {self.gestacion_dias} días"
        )


# Subclase Ave
class Ave(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, puede_volar):
        super().__init__(nombre, edad, peso)
        self.puede_volar = puede_volar

    def saluda(self):
        if self.puede_volar:
            print(f"Soy un ave llamado {self.nombre} y puedo volar")
        else:
            print(f"Soy un ave llamado {self.nombre} y no puedo volar")


# Programa principal
def main():
    animal1 = AnimalTerrestre("Kuma", 5, 120)
    animal2 = Mamifero("Miu", 3, 25, 90)
    animal3 = Ave("Pío", 2, 1.5, True)

    # Lista de animales (polimorfismo)
    animales = [animal1, animal2, animal3]

    # Llamada al mismo método
    for animal in animales:
        animal.saluda()


main()
