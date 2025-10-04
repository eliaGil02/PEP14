"""
Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de
millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los
resultados deben estar redondeados a 2 decimales.
"""

millas = float(input("Introduce el número de millas: "))
km = float(input("Introduce el número de kilómetros: "))

millasAKm = millas * 1.61
kmAMillas = km / 1.61

print("Millas a Km:", round(millasAKm, 2))
print("Km a Millas:", round(kmAMillas, 2))
