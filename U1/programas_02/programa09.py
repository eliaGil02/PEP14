"""
Escribe un programa que calcule la calificación de estudiante en un módulo. La
calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3
20%).
"""

ra1 = float(input("Introduce la nota de RA1 (20%): "))
ra2 = float(input("Introduce la nota de RA2 (60%): "))
ra3 = float(input("Introduce la nota de RA3 (20%): "))

nota_final = (ra1 * 0.20) + (ra2 * 0.60) + (ra3 * 0.20)

print("La calificación final es:", nota_final)
