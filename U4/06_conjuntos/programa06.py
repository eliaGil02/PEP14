"""
Escribe un programa en Python que realice las siguientes operaciones con conjuntos.
 Crea tres conjuntos diferentes.
 Usa los métodos issubset(), issuperset() e isdisjoint() para verificar
relaciones entre ellos.
 Muestra los resultados de cada comprobación.
"""

# definir conjuntos
A = {1, 2}
B = {1, 2, 3}
C = {4, 5}

# comprobar subconjunto
print(A.issubset(B))

# comprobar superconjunto
print(B.issuperset(A))

# comprobar conjuntos disjuntos
print(A.isdisjoint(C))