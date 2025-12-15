from abc import ABC, abstractmethod
import random


# =========================
# CLASE BASE ABSTRACTA
# =========================
class Personaje(ABC):
    def __init__(self, nombre, vida):
        self._nombre = nombre
        self._vida = vida

    @property
    def nombre(self):
        return self._nombre

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, valor):
        # La vida nunca puede ser negativa
        if valor < 0:
            self._vida = 0
        else:
            self._vida = valor

    @property
    def vivo(self):
        return self._vida > 0

    @abstractmethod
    def atacar(self, objetivo):
        pass


# =========================
# CLASE ARMA (COMPOSICIÓN)
# =========================
class Arma:
    def __init__(self, nombre, danio):
        self._nombre = nombre
        self._danio = danio

    @property
    def nombre(self):
        return self._nombre

    @property
    def danio(self):
        return self._danio


# =========================
# SUBCLASE GUERRERO
# =========================
class Guerrero(Personaje):
    def __init__(self, nombre, vida, arma):
        super().__init__(nombre, vida)
        self._arma = arma

    @property
    def arma(self):
        return self._arma

    def atacar(self, objetivo):
        # Daño del arma + pequeño bonus aleatorio
        bonus = random.randint(1, 5)
        danio_total = self.arma.danio + bonus
        objetivo.vida -= danio_total

        print(
            f"{self.nombre} ataca con {self.arma.nombre} "
            f"y causa {danio_total} de daño a {objetivo.nombre}"
        )


# =========================
# SUBCLASE MAGO
# =========================
class Mago(Personaje):
    def __init__(self, nombre, vida, hechizos):
        super().__init__(nombre, vida)
        self._hechizos = hechizos

    @property
    def hechizos(self):
        return self._hechizos

    def atacar(self, objetivo):
        # Elegir hechizo al azar
        hechizo, danio = random.choice(list(self.hechizos.items()))
        objetivo.vida -= danio

        print(
            f"{self.nombre} lanza {hechizo} "
            f"y causa {danio} de daño a {objetivo.nombre}"
        )
