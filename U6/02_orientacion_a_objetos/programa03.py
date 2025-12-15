"""
Crea un módulo en python que implemete las siguienetes clases:
 Clase abstracta AnimalMarino con:
◦ Atributos de instancia: nombre.
◦ Define propiedades (get y set) para el atributo (usando decoradores @property)
◦ Método abstracto sonido()
◦ Método abstracto saluda()
 Subclase Delfin.
◦ Constructor __init__(self, nombre)
◦ Implementa los métodos abstractos.
▪ Método sonido(): muestra "Clicks y silbidos"
▪ Método saluda(): muestra algo como “Soy un delfin llamado
Alex.”
 Subclase Tiburón.
◦ Constructor __init__(self, nombre)
◦ Implementa los métodos abstractos
▪ Método sonido(): muestra "No tiene un sonido audible característico"
▪ Método saluda(): muestra algo como ”Soy un tiburón llamado Mai.”
Escribe un programa que importe el módulo y crre una función main que.
 Cree una lista con varios objetos Delfin y Tiburón.
 Recorra la lista y llame a los métodos saluda y sonido por cada objeto.
"""

from abc import ABC, abstractmethod


# Clase abstracta
class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    # Método abstracto
    @abstractmethod
    def saluda(self):
        pass


# Subclase Mamifero
class Mamifero(Animal):
    def saluda(self):
        print(f"Soy un mamífero llamado {self.nombre}")


# Subclase Ave
class Ave(Animal):
    def saluda(self):
        print(f"Soy un ave llamado {self.nombre}")


# Programa principal
def main():
    animal1 = Mamifero("Kuma")
    animal2 = Ave("Pío")

    animales = [animal1, animal2]

    for animal in animales:
        animal.saluda()


main()
