"""
Escribe un programa en Python que realice las siguientes operaciones con listas.
 Crear una lista con dos elementos que a su vez sean una lista con los 100 primeros
números pares y otra lista con los 100 primeros números impares.
◦ Usa un for para crearla.
◦ Usa compresión de listas para crearla.
 Recorre la lista y muestra por pantalla todos sus elementos: en una línea todos los
números pares y en otra los impares.
"""

# for
pares = []
impares = []

for i in range(1, 201):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

lista = [pares, impares]

# compresion de listas
pares_comp = [i for i in range(2, 201, 2)]
impares_comp = [i for i in range(1, 200, 2)]

lista_comp = [pares_comp, impares_comp]


# recorrer y mostrar
for num in lista[0]:
    print(num, end=" ")


for num in lista[1]:
    print(num, end=" ")
