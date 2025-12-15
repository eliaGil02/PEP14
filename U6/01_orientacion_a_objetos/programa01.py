"""
Escribe un programa en Python que :
 Cree una clase Animal con:
◦ Atributos de instancia: nombre, especie y edad
◦ Constructor __init__(self, nombre, especie, edad)
◦ Método de instancia saluda que muestre algo como:
          Soy un tigre llamado Kuma y tengo 5 años.
◦ Método de instancia cumplir_anios que aumente en 1 la edad.
 Crea una función main que:
◦ Cree dos animales distintos.
◦ Muestre su nombre, edad y especie.
◦ Llame a saluda() y luego a cumplir_anios() para cada uno.
◦ Cambie el nombre del un animal y que se presente de nuevo.
"""


# definicion de la clase
class Animal:
    # constructor
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    # metodo para mostrar info
    def saluda(self):
        print(f"Soy un {self.especie} llamado {self.nombre} y tengo {self.edad} años.")

    # metodo para incrementar edad
    def cumplir_anios(self):
        self.edad += 1


# programa principal
def main():
    # creacion de objetos
    animal1 = Animal("Kuma", "tigre", 5)
    animal2 = Animal("Luna", "perro", 3)

    # Acceso a atributos
    print(animal1.nombre, animal1.especie, animal1.edad)
    print(animal2.nombre, animal2.especie, animal2.edad)

    # métodos
    animal1.saluda()
    animal1.cumplir_anios()

    animal2.saluda()
    animal2.cumplir_anios()

    # modificicacion de un atributo
    animal1.nombre = "Max"
    animal1.saluda()


main()
