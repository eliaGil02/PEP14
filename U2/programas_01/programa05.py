"""
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor
o que indique que son iguales.
"""

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 < num2:
    print("El menor es:", num1, "y el mayor es:", num2)
elif num1 > num2:
    print("El menor es:", num2, "y el mayor es:", num1)
else:
    print("Ambos números son iguales")
