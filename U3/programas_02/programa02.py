"""
Modifica el programa anterior para que solo se importen las funciones del módulo math
que se usan en el programa.
"""

from math import sin, cos, sqrt, pow, radians

print("¿Qué quieres hacer?")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada")
print("4. Potencia (base y exponente)")

opcion = int(input("Elige una opción (1-4): "))

if opcion == 1:
    angulo = float(input("Dime el ángulo en grados: "))
    resultado = sin(radians(angulo))
    print(f"El seno de {angulo}° es {resultado}")

elif opcion == 2:
    angulo = float(input("Dime el ángulo en grados: "))
    resultado = cos(radians(angulo))
    print(f"El coseno de {angulo}° es {resultado}")

elif opcion == 3:
    numero = float(input("Dime el número: "))
    resultado = sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {resultado}")

elif opcion == 4:
    base = float(input("Base: "))
    exponente = float(input("Exponente: "))
    resultado = pow(base, exponente)
    print(f"{base} elevado a {exponente} es {resultado}")

else:
    print("Esa opción no vale")
