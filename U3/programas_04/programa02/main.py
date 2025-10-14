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

from matematicas import (
    suma,
    resta,
    multiplicacion,
    division,
    area_rectangulo,
    area_triangulo,
    area_circulo,
    conversiones,
)


def main():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1) Operaciones matemáticas")
        print("2) Cálculo de áreas geométricas")
        print("0) Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            print("\n1) Sumar  2) Restar  3) Multiplicar  4) Dividir")
            print("5) A binario  6) A hexadecimal  7) Texto a entero")
            sub = input("Opción: ")

            if sub in {"1", "2", "3", "4"}:
                a = float(input("a: "))
                b = float(input("b: "))
                if sub == "1":
                    print("Resultado:", suma(a, b))
                elif sub == "2":
                    print("Resultado:", resta(a, b))
                elif sub == "3":
                    print("Resultado:", multiplicacion(a, b))
                elif sub == "4":
                    print("Resultado:", division(a, b))
            elif sub == "5":
                n = int(input("Entero: "))
                print("Binario:", conversiones.a_binario(n))
            elif sub == "6":
                n = int(input("Entero: "))
                print("Hexadecimal:", conversiones.a_hexadecimal(n))
            elif sub == "7":
                texto = input("Texto: ")
                print("Entero:", conversiones.a_entero(texto))
        elif opcion == "2":
            print("\n1) Rectángulo  2) Triángulo  3) Círculo")
            sub = input("Opción: ")
            if sub == "1":
                b = float(input("Base: "))
                h = float(input("Altura: "))
                print("Área:", area_rectangulo(b, h))
            elif sub == "2":
                b = float(input("Base: "))
                h = float(input("Altura: "))
                print("Área:", area_triangulo(b, h))
            elif sub == "3":
                r = float(input("Radio: "))
                print("Área:", area_circulo(r))
        elif opcion == "0":
            print("Adiós!")
            break


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
