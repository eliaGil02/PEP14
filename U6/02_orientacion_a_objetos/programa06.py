"""
Basándote en los programas anteriores, crea:
 Ejemplo de dependencia
◦ Una clase utiliza otra solo durante la ejecución de un método.
◦ No guarda el objeto, no lo conserva, no lo controla.
◦ Clase Veterinario con:
▪ Atributos de instancia: nombre.
▪ Constructor __init__(self, nombre)
▪ Define propiedades (get y set) para el atributo (usando decoradores
@property)
▪ Método revisar(animal) que imprime: “Revisando a
          <animal.nombre>2
 Ejemplo de agregación
◦ Una clase almacena referencias a objetos creados externamente.
◦ No los crea ni los destruye, solo los “tiene”
◦ Clase ReservaNatural con:
▪ Atributos de instancia: lista_animales.
▪ Constructor __init__(self, lista_animales)
▪ Métodos añadir(animal).
.
 Ejemplo de composición
◦ Aquí el todo crea y controla sus partes internas.
◦ Las partes no existen fuera del Tiburón.
◦ Clase Corazon con:
▪ Atributos de instancia: tamaño.
▪ Constructor __init__(self, tamaño)
▪ Método late(): muestra “estoy latiendo”
◦ Clase Pulmones con:
▪ Atributos de instancia: tamaño.
▪ Constructor __init__(self, tamaño)
▪ Método respira(): muestra “estoy latiendo”
◦ Clase Corazon con:
▪ Atributos de instancia: tamaño.
▪ Constructor __init__(self, tamaño)
▪ Método latidos(): muestra “estoy latiendo”
◦ Amplia la clase Tiburón.
▪ Artributos de instancia:
 corazón : objeto de la clase Corazon.
 pulmone : objeto de la clase Pulmones.
▪ Constructor __init__(self, nombre). Crear los objetos de tipo Corazon y Pulmones.
▪ Método nadar(). Llama a los métodos late() y respita() del corazon y del pulmon.
 Crea una función main que:
◦ Cree varios objetos de las clases anteriores y pruebe su comportamiento.
"""


# Clase independiente
class Profesor:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        print(f"Profesor: {self.nombre}")


# Clase que agrega profesores
class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.profesores = []

    # Método para añadir un profesor (agregación)
    def anadir_profesor(self, profesor):
        self.profesores.append(profesor)

    def mostrar_info(self):
        print(f"Departamento: {self.nombre}")
        for profesor in self.profesores:
            profesor.mostrar_info()


# Programa principal
def main():
    prof1 = Profesor("Ana")
    prof2 = Profesor("Luis")

    departamento = Departamento("Informática")

    departamento.anadir_profesor(prof1)
    departamento.anadir_profesor(prof2)

    departamento.mostrar_info()


main()
