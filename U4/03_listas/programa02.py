"""
Escribe un programa en Python que realice las siguientes operaciones con listas
partiendo el programa anterior:
 Partiendo de mi_listaXX del ejercicio anterior modifica el valor del tercer elemento a
un nuevo valor de tu elección.
 Añade un nuevo elemento al final de la lista utilizando el método append().
 Inserta una nueva cadena de caracteres en la segunda posición de la lista (índice
1) utilizando el método insert().
 Recorre la lista y muestra sus elementos por pantalla.
"""

# crear la lista
mi_lista14 = [10, "Python", False, 3.14]

# modificar tercer elemento
mi_lista14[2] = True

# añadir un elemento
mi_lista14.append(25)

# insertar una cadena en segunda posicion
mi_lista14.insert(1, "elemento")

# recorrer la lista y mostrar
for elemento in mi_lista14:
    print(elemento)
