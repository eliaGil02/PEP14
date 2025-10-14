"""
Escribe un programa en Python que importe el modulo math completo y que le pregunte al
usuario que operación matemática quiere hacer:
1. Seno de un ángulo
2. Coseno de ángulo
3. Raíz cuadrada de un número
4. Potencia de dos números.
Le pida los datos necesarios y muestre los resultados por pantalla.
"""

import math

print("¿Qué quieres hacer?")
print("1. Seno de un ángulo")
print("2. Coseno de un ángulo")
print("3. Raíz cuadrada")
print("4. Potencia (base y exponente)")

opcion = int(input("Elige una opción (1-4): "))

if opcion == 1:
    angulo = float(input("Dime el ángulo en grados: "))
    resultado = math.sin(math.radians(angulo))
    print(f"El seno de {angulo}° es {resultado}")

elif opcion == 2:
    angulo = float(input("Dime el ángulo en grados: "))
    resultado = math.cos(math.radians(angulo))
    print(f"El coseno de {angulo}° es {resultado}")

elif opcion == 3:
    numero = float(input("Dime el número: "))
    resultado = math.sqrt(numero)
    print(f"La raíz cuadrada de {numero} es {resultado}")

elif opcion == 4:
    base = float(input("Base: "))
    exponente = float(input("Exponente: "))
    resultado = math.pow(base, exponente)
    print(f"{base} elevado a {exponente} es {resultado}")

else:
    print("Esa opción no vale")
