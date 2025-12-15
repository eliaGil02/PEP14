"""
Escribe un programa en Python que :
 Modifique la clase Animal
◦ Añade al constructor un parámetro peso y guarda el valor en un atributo privado.
◦ Modifica los get y set del parámetro id_chip para propiedades (usando decoradores @property).
◦ Define propiedades (get, set y delete) para el atributo peso (usando decoradores @property)
 Crea una función main que:
◦ Cree un Animal con peso inicial.
◦ Muestre el peso
◦ Cambie el peso.
◦ Elimina el peso y comprueba qué ocurre si se intenta mostrar el peso.
"""


# clase animal usando propiedades
class Animal:
    def __init__(self, nombre, especie, edad, id_chip, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.__id_chip = id_chip
        self.__peso = peso

    # propiedad para id
    @property
    def id_chip(self):
        return self.__id_chip

    @id_chip.setter
    def id_chip(self, nuevo_id):
        if nuevo_id == "":
            raise ValueError("El id_chip no puede estar vacío")
        self.__id_chip = nuevo_id

    # propiedad para peso
    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, nuevo_peso):
        self.__peso = nuevo_peso

    @peso.deleter
    def peso(self):
        del self.__peso


def main():
    animal = Animal("Kuma", "tigre", 5, "ABC123", 120.5)

    print("Peso:", animal.peso)

    animal.peso = 130.0
    print("Nuevo peso:", animal.peso)

    # eliminar atributo
    del animal.peso

    try:
        print(animal.peso)
    except AttributeError as e:
        print("Error:", e)


main()
