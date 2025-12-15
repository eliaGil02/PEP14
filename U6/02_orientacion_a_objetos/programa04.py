"""
 Amplía la clase AnimalTerrestre:
◦ Implementa __str__(self) en la clase padre y las clases hijas para que
print(animal) muestre algo como: AnimalTerrestre(nombre='Kuma',edad=5, peso=120.0)
     Mamífero(nombre='Kuma',edad=5, peso=120.0)
◦ Implementa un método mágico de comparación, por ejemplo: def __lt__(self, otro) teniendo en cuenta que un animal es 'menor' que otro si su edad es menor.
◦ Implementa __add__(self, otro) que devuelva un nuevo animal que combine a dos:
 nombre: concatenación de nombres ("Kuma-Balto")
 edad: media de ambas edades (entera o float, como prefieras)  peso: suma de los pesos (si existen, si no, None).
 Crea una función main que:
◦ Cree varios animales, mamiferos y aves con edad y peso.
◦ Los compare con < (por ejemplo, animal1 < animal2).
◦ Cree un “animal combinado” con animal3 = animal1 + animal2 y lo
muestre con print(animal3).
"""


# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def saluda(self):
        print(f"Soy un animal llamado {self.nombre}")


# Subclase
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    # Sobrescritura del método
    def saluda(self):
        # Llamada al método de la clase base
        super().saluda()
        # Comportamiento adicional
        print(f"Soy un perro de raza {self.raza}")


# Programa principal
def main():
    animal = Animal("Kuma")
    perro = Perro("Rocky", "Labrador")

    animal.saluda()
    perro.saluda()


main()
