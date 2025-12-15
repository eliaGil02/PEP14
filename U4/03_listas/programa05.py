"""
Escribe un programa en Python que realice las siguientes operaciones con listas.
 Ordenación Modificable vs. no modificable:
◦ Crea una lista de cadenas no ordenadas. Utiliza el método sort() para
ordenar la lista y comprueba que la lista original ha sido modificada.
◦ Utiliza la función sorted() y comprueba que la lista original no se modifica.
 Concatenación
◦ Crea dos listas y crea una nueva lista que se la concatenación de las anteriores.
◦ Crea dos listas y amplia la primera añadiendo los elementos de las segunda
 Diferencia de copia:
◦ Asigna tu lista original a una nueva variable utilizando una asignación directa
(copia = lista). Muestra los identificadores de memoria de ambas variables
usando id() para verificar que apuntan al mismo objeto.
"""

# lista desordenada
lista = ["pera", "manzana", "kiwi", "naranja"]

# ordenacion modificable con sort
lista.sort()
print(lista)

# lista desordenada x2
lista2 = ["pera", "manzana", "kiwi", "naranja"]

# ordenacion no modificable con sorted
lista_ordenada = sorted(lista2)
print(lista2)
print(lista_ordenada)

# concatenacion
l1 = [1, 2, 3]
l2 = [4, 5, 6]

lista_concatenada = l1 + l2
print(lista_concatenada)

# ampliar la primera lista con la segunda
l1.extend(l2)
print(l1)

# diferencia de copia
l_original = [10, 20, 30]
copia = l_original
print(id(l_original), id(copia))
