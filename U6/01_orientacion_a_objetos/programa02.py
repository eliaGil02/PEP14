"""
Escribe un programa en Python que :
 Amplíe la clase Animal para manejar un atributo no público:
◦ Añade al constructor un parámetro id_chip y guarda el valor en un atributo privado.
◦ Implementa los métodos:
▪ get_id_chip(self) → devuelve el id_chip. ▪ set_id_chip(self, nuevo_id)
 Solo acepta valores de tipo str no vacíos.
 Si el valor no es del tipo adecuado lanza una excepción de tipo
TypeError.
 Si el valor no es un id_chip adecuado lanza una excepción del tipo
ValueError.
 Crea una función main que:
◦ Cree un Animal con un id_chip inicial.
◦ Muestra el chip con get_id_chip().
◦ Intenta cambiarlo por:
▪ un valor válido (por ejemplo "ABC123"),
▪ un valor no válido (por ejemplo 123 o ""), y comprueba el comportamiento.
Recuerda: el atributo sigue siendo accesible con _Animal__id_chip, pero no se debe usar en el código normal.
"""


# definicion de la clase
class Animal:
    # constructor
    def __init__(self, nombre, especie, edad, id_chip):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

        # atributo privado
        self.__id_chip = id_chip

    # getter
    def get_id_chip(self):
        return self.__id_chip

    # setter con validacion
    def set_id_chip(self, nuevo_id):
        if not isinstance(nuevo_id, str):
            raise TypeError("El id_chip debe ser una cadena")
        if nuevo_id == "":
            raise ValueError("El id_chip no puede estar vacío")
        self.__id_chip = nuevo_id


def main():
    animal = Animal("Kuma", "tigre", 5, "ABC123")

    # acceso mediante getter
    print("ID chip:", animal.get_id_chip())

    # modificacion correcta
    animal.set_id_chip("XYZ999")
    print("Nuevo ID chip:", animal.get_id_chip())

    # pruebas de error
    try:
        animal.set_id_chip(123)
    except Exception as e:
        print("Error:", e)

    try:
        animal.set_id_chip("")
    except Exception as e:
        print("Error:", e)


main()
