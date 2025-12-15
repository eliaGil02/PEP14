"""
Escribe un programa en Python que permita crear una lista de palabras y que, a
continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
"""

lista_palabras = ["hola", "adios", "python", "hola", "java"]

# pedir una palabra
buscar = input("Introduce la palabra a buscar: ")

# contar cuantas veces aparece
contador = lista_palabras.count(buscar)

print(f"La palabra aparece {contador} vez")
