"""
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).
"""

mensajeGlobal = "Soy una variable global"


def funcionExterna():
    mensajeExterno = "Soy una variable local de la función externa"

    def funcionInterna():
        nonlocal mensajeExterno
        mensajeExterno = "Soy una variable no local modificada en la función interna"
        mensajeInterno = "Soy una variable local de la función interna"

        print("\n--- Dentro de la función interna ---")
        print(mensajeGlobal)
        print(mensajeExterno)
        print(mensajeInterno)

    funcionInterna()

    print("\n--- Dentro de la función externa ---")
    print(mensajeGlobal)
    print(mensajeExterno)


def main():
    print("--- En el ámbito global ---")
    print(mensajeGlobal)
    funcionExterna()
    print("\n--- De nuevo en el ámbito global ---")
    print(mensajeGlobal)


if __name__ == "__main__":
    main()
