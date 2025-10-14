from .operaciones import suma, resta, multiplicacion, division
from .figuras import area_rectangulo, area_triangulo, area_circulo
from . import conversiones

__version__ = "1.0.0"
__all__ = [
    "suma",
    "resta",
    "multiplicacion",
    "division",
    "area_rectangulo",
    "area_triangulo",
    "area_circulo",
    "conversiones",
]


def info():
    return f"Paquete matematicas versión {__version__}"


def _demo():
    print(info())
    print("suma(2,3) =", suma(2, 3))
    print("area_rectangulo(4,5) =", area_rectangulo(4, 5))
    print("a_binario(10) =", conversiones.a_binario(10))


if __name__ == "__main__":
    _demo()
