"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
"""

import math


def mostrar_menu():
    print("\n---MENÚ---")
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Introduce una opción (1-4): "))
            if opcion == 1:
                opcion1()
            elif opcion == 2:
                opcion2()
            elif opcion == 3:
                opcion3()
            elif opcion == 4:
                print("Hasta luego")
                break
            else:
                print("Opción no válida. Debe ser un número entre 1 y 4.")
        except ValueError:
            print("Debes introducir un número válido.")


def calcular_area_circulo(radio):
    return math.pi * radio**2


def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def calcular_area_rectangulo(base, altura):
    return base * altura


def pedir_valor_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor que 0.")
        except ValueError:
            print("Debes introducir un número válido.")


def opcion1():
    radio = pedir_valor_positivo("Introduce el radio del círculo: ")
    area = calcular_area_circulo(radio)
    print(f"El área del círculo es: {area:.2f}")


def opcion2():
    base = pedir_valor_positivo("Introduce la base del triángulo: ")
    altura = pedir_valor_positivo("Introduce la altura del triángulo: ")
    area = calcular_area_triangulo(base, altura)
    print(f"El área del triángulo es: {area:.2f}")


def opcion3():
    base = pedir_valor_positivo("Introduce la base del rectángulo: ")
    altura = pedir_valor_positivo("Introduce la altura del rectángulo: ")
    area = calcular_area_rectangulo(base, altura)
    print(f"El área del rectángulo es: {area:.2f}")


if __name__ == "__main__":
    main()
