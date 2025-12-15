"""
Escribe un programa en Python que:
 Amplíe la clase Animal
◦ Crea un atributo de clase: numero_animales = 0
◦ En el __init__, cada vez que se cree un Animal, incrementa
Animal.numero_animales.
▪ Crea un método de clase:
          @classmethod
          def contar_animales(cls):
               return cls.numero_animales
 Crea un método estático:
  @staticmethod
  def es_mayor_de_edad(edad):
        "Devuelve True si el animal se considera adulto (≥ 2
            años)."
        return edad >= 2
 Crea una función main que:
◦ Cree varios animales.
◦ Muestre cuántos animales hay creados usando:
       Animal.contar_animales()
◦ Compruebe el método estático.
"""


# clase animal con atributos y métodos de clase
class Animal:
    # atributo de clase
    numero_animales = 0

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        Animal.numero_animales += 1

    # metodo de clase
    @classmethod
    def contar_animales(cls):
        return cls.numero_animales

    # metodo estatico
    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 2


def main():
    a1 = Animal("Kuma", "tigre", 5)
    a2 = Animal("Luna", "perro", 1)

    print("Número de animales:", Animal.contar_animales())

    print("Kuma adulto: ", Animal.es_mayor_de_edad(a1.edad))
    print("Luna adulta: ", Animal.es_mayor_de_edad(a2.edad))


main()
