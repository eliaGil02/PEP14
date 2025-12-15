"""
Escribe un programa en Python que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
"""

# pedir una frase al usuario
frase = input("Introduce una frase: ")

# separar la frase en palabras
palabras = frase.split()

# diccionario para contar palabras
frecuencia = {}

# recorrer las palabras
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

# mostrar la frecuencia de cada palabra
for palabra, contador in frecuencia.items():
    print(palabra, ":", contador)
