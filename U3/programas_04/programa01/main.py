"""
Crea un paquete llamado matemáticas que contenga tres módulos:
 operaciones: creado en la práctica anterior.
 figuras: tendrá las siguientes funciones.
◦ area_rectangulo(base, altura): devuelve el área.
◦ area_triangulo(base, altura): devuelve el área.
◦ area_circulo(radio): devuelve el área.
 conversiones.py: tendrá las siguientes funciones
◦ a_binario(n): devuelve la representación binaria de un número entero en forma
de cadena.
◦ a_hexadecimal(n): devuelve la representación hexadecimal de un número
entero en forma de cadena.
◦ a_entero(texto): convierte una cadena numérica en un entero (controlando
errores si el texto no es válido)

Recuerda que debes incluir el fichero __init__.py aunque esté vacío.
Crea un programa principal main.py que muestre un menú que permita elegir entre:
 Operaciones matemáticas
 Cálculo de áreas geométricas

Según la opción elegida, pida al usuario los datos necesarios y muestre el resultado
correspondiente.
El programa principal (main,py) debe seguir la estructura.
"""

# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios

from matematicas import figuras, conversiones
from matematicas.operaciones import sumar, restar, multiplicar, dividir, potencia


def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Operaciones matemáticas")
        print("2) Cálculo de áreas geométricas")
        print("0) Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            print("\n1) Sumar")
            print("2) Restar")
            print("3) Multiplicar")
            print("4) Dividir")
            print("5) Potencia")
            print("6) A binario")
            print("7) A hexadecimal")
            print("8) Texto a entero")
            sub = input("Elige una opción: ")

            if sub in {"1", "2", "3", "4", "5"}:
                a = float(input("a: "))
                b = float(input("b: "))

                if sub == "1":
                    print("Resultado:", sumar(a, b))
                elif sub == "2":
                    print("Resultado:", restar(a, b))
                elif sub == "3":
                    print("Resultado:", multiplicar(a, b))
                elif sub == "4":
                    print("Resultado:", dividir(a, b))
                elif sub == "5":
                    print("Resultado:", potencia(a, b))

            elif sub == "6":
                n = int(input("Introduce un número entero: "))
                print("Binario:", conversiones.a_binario(n))

            elif sub == "7":
                n = int(input("Introduce un número entero: "))
                print("Hexadecimal:", conversiones.a_hexadecimal(n))

            elif sub == "8":
                texto = input("Introduce una cadena numérica: ")
                print("Entero:", conversiones.a_entero(texto))

        elif opcion == "2":
            print("\n1) Rectángulo")
            print("2) Triángulo")
            print("3) Círculo")
            sub = input("Elige una figura: ")

            if sub == "1":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("Área:", figuras.area_rectangulo(base, altura))
            elif sub == "2":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print("Área:", figuras.area_triangulo(base, altura))
            elif sub == "3":
                radio = float(input("Radio: "))
                print("Área:", figuras.area_circulo(radio))

        elif opcion == "0":
            print("¡Adiós!")
            break


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
