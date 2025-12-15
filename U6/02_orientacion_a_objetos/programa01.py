"""
Crea un módulo en python que implemete las siguienetes clases:
 Clase AnimalTerrestre con:
◦ Atributos de instancia: nombre,edad y peso
◦ Define propiedades (get y set) para los atributos (usando decoradores
@property)
◦ Constructor __init__(self, nombre, edad, peso)
◦ Método de instancia saluda que muestre algo como “ Soy un animal
        terrestre llamado Kuma y tengo 5 años.”
 Subclase Mamifero
◦ Añade el atributo de instancia: gestacion_dias.
◦ Constructor __init__(self, nombre, edad, peso,
        gestacion_dias)
◦ Define propiedades (get y set) para el atributo (usando decoradores @property)
◦ Sobrescribe saluda para que muestre algo como:”Soy un mamifero llamado Kuma, tengo 5 años y mi gestación dura 100 días.”
 Subclase Ave
◦ Añade el atributo de instancia: puede_volar (booleano).
◦ Constructor __init__(self, nombre, edad, peso, puede_volar)
◦ Define propiedades (get y set) para el atributo (usando decoradores @property)
◦ Sobrescribe saluda para que muestre algo como:” Soy un ave llamado Mau, tengo 2 años y no puedo volar.
Escribe un programa que importe el módulo y crre una función main() que.
 Cree un Animal, una Mamifero y un Ave.
 Llame al método saluda para cada uno de ellos.
"""


# Clase base
class AnimalTerrestre:
    def __init__(self, nombre, edad, peso):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso

    # Propiedades
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self, valor):
        self._peso = valor

    # Método de instancia
    def saluda(self):
        print(
            f"Soy un animal terrestre llamado {self.nombre} y tengo {self.edad} años."
        )


# Subclase Mamifero
class Mamifero(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, gestacion_dias):
        super().__init__(nombre, edad, peso)
        self.gestacion_dias = gestacion_dias

    @property
    def gestacion_dias(self):
        return self._gestacion_dias

    @gestacion_dias.setter
    def gestacion_dias(self, valor):
        self._gestacion_dias = valor

    # Sobrescritura del método
    def saluda(self):
        print(
            f"Soy un mamífero llamado {self.nombre}, tengo {self.edad} años "
            f"y mi gestación dura {self.gestacion_dias} días."
        )


# Subclase Ave
class Ave(AnimalTerrestre):
    def __init__(self, nombre, edad, peso, puede_volar):
        super().__init__(nombre, edad, peso)
        self.puede_volar = puede_volar

    @property
    def puede_volar(self):
        return self._puede_volar

    @puede_volar.setter
    def puede_volar(self, valor):
        self._puede_volar = valor

    # Sobrescritura del método
    def saluda(self):
        if self.puede_volar:
            print(
                f"Soy un ave llamado {self.nombre}, tengo {self.edad} años y puedo volar."
            )
        else:
            print(
                f"Soy un ave llamado {self.nombre}, tengo {self.edad} años y no puedo volar."
            )


# Programa principal
def main():
    animal = AnimalTerrestre("Kuma", 5, 120.0)
    mamifero = Mamifero("Kuma", 5, 120.0, 100)
    ave = Ave("Mau", 2, 3.5, False)

    animal.saluda()
    mamifero.saluda()
    ave.saluda()


main()
