"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Crea dos conjuntos A y B con números.
 Muestra la unión (A | B), la intersección (A & B), la diferencia (A - B) y la
diferencia simétrica (A ^ B).
 Repite las operaciones usando los métodos union(), intersection(), difference() y symmetric_difference()
"""

# definir dos conjuntos
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# unión
print(A | B)

# intersección
print(A & B)

# diferencia
print(A - B)

# diferencia simétrica
print(A ^ B)

# mismas operaciones con métodos
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))
