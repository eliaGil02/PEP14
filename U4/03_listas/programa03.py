"""
Escribe un programa en Python que realice las siguientes operaciones con listas
partiendo del programa anterior.
 Crea una nueva lista extrayendo un slice de los elementos desde el índice 2 hasta
el índice 5 (recuerda que el índice final es excluido).
 Muestra una nueva lista que contenga solo los elementos de tu lista original que
estén en posiciones pares, utilizando un incremento de 2 en el slicing.
 Reverso
◦ Crear nueva lista en orden inverso utilizando la sintaxis de slicing [::-1].
◦ Usa el método reverse() para invertir la lista y modificar su contenido.
"""

# lista
mi_lista14 = [10, "elemento", "Python", True, 3.14, 25]

# slice desde 2 hasta 5
slice_lista = mi_lista14[2:5]
print(slice_lista)

# elementos en posiciones pares usando slicing
pares = mi_lista14[::2]
print(pares)

# reverso usando slicing
lista_invertida = mi_lista14[::-1]
print(lista_invertida)

# reverso usando reverse()
mi_lista14.reverse()
print(mi_lista14)
