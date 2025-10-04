"""
Escribe un programa que use varias veces la función printf() para
 Mostrar las operaciones del los operadores aritméticos de Python entre dos
números.
 Mostrar las operaciones de los operadores lógicos de Python con valores
booleanos.
 Mostrar las operaciones de los operadores de comparación de Python con valores
booleanos y/o números.
"""

a = 10
b = 3

print("--- Operadores Aritméticos ---")
print("Suma: %d" % (a + b))
print("Resta: %d" % (a - b))
print("Multiplicación: %d" % (a * b))
print("División: %.2f" % (a / b))  # con 2 decimales
print("División entera: %d" % (a // b))
print("Módulo: %d" % (a % b))
print("Potencia: %d" % (a**b))

x = True
y = False

print("\n--- Operadores Lógicos ---")
print("AND lógico: %s" % (x and y))
print("OR lógico: %s" % (x or y))
print("NOT lógico: %s" % (not x))

print("\n--- Operadores de Comparación ---")
print("Igualdad (==): %s" % (a == b))
print("Distinto (!=): %s" % (a != b))
print("Mayor (>): %s" % (a > b))
print("Menor (<): %s" % (a < b))
print("Mayor o igual (>=): %s" % (a >= b))
print("Menor o igual (<=): %s" % (a <= b))
