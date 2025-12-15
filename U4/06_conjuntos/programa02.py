"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Crea un conjunto con varias frutas.
 Añade nuevos elementos usando add().
 Elimina un elemento existente usando remove().
 Usa discard() para eliminar un elemento que no exista (sin error).
 Usa pop() para eliminar un elemento aleatorio..
"""

# conjunto inicial de frutas
frutas = {"manzana", "pera", "plátano"}

# añadir un elemento
frutas.add("naranja")

# eliminar un elemento existente
frutas.remove("pera")

# eliminar sin error si no existe
frutas.discard("kiwi")

# eliminar un elemento aleatorio
frutas.pop()

print(frutas)
