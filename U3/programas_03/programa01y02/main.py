"""
Crea un módulo llamado operaciones que contenga cuatro funciones básicas
relacionadas con operaciones numéricas:
 suma(a, b) → devuelve la suma de dos números.
 resta(a, b) → devuelve la resta de dos números.
 multiplicacion(a, b) → devuelve la multiplicación de dos números.
 division(a, b) → devuelve la división de dos números (controlando la división entre
cero).
Crea un programa principal main.py que y importe el módulo matemáticas, pida al usuario
dos números y muestre los resultados de aplicar cada una de las funciones anteriores.
Modifica el programa principal (main,py) del ejercicio anterior para que siga la siguiente
estructura.
"""

# imports de la librería estándar
# imports de librerías de terceros
# imports de módulos propios
import operaciones


# Definición de funciones principales
def main():
    """Función principal del programa"""
    print("Operaciones matemáticas:")

    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print("Suma:", operaciones.suma(a, b))
    print("Resta:", operaciones.resta(a, b))
    print("Multiplicación:", operaciones.multiplicacion(a, b))
    print("División:", operaciones.division(a, b))


# Bloque para asegurar ejecución sólo si el archivo es el principal
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
