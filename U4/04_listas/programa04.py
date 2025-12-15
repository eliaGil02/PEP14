"""
Escribe un programa en Python que permita crear dos listas de palabras y que, a
continuación, escriba las siguientes listas (en las que no debe haber repeticiones):
• Lista de palabras que aparecen en las dos listas.
• Lista de palabras que aparecen en la primera lista, pero no en la segunda.
• Lista de palabras que aparecen en la segunda lista, pero no en la primera.
• Lista de palabras que aparecen en ambas listas.
Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos
repetidos en cada lista
"""

# crear dos listas
lista1 = ["python", "java", "c", "python", "java"]
lista2 = ["java", "c++", "python", "python", "go"]

# eliminar repeticiones usando conjuntos
set1 = set(lista1)
set2 = set(lista2)

# palabras que aparecen en las dos listas
ambas = list(set1 & set2)

# palabras que aparecen en la primera solo
primera = list(set1 - set2)

# palabras que aparecen en la segunda solo
segunda = list(set2 - set1)

print(ambas)
print(primera)
print(segunda)
