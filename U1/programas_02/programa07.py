"""
Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a
cuantas horas y minutos corresponde.
"""

minutos = int(input("Introduce la cantidad de minutos: "))

horas = minutos // 60
resto_minutos = minutos % 60

print(minutos, "minutos son", horas, "horas y", resto_minutos, "minutos")
