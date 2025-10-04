"""
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la
suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza
la instrucción break y otra no.
"""

# con break
suma = 0.0
contador = 0
while True:
    x = float(input("Introduce un número (0 para terminar): "))
    if x == 0:
        break
    suma += x
    contador += 1
media = suma / contador if contador > 0 else 0
print("Suma:", suma)
print("Media:", media)

# sin break
suma = 0.0
contador = 0
x = None
while x != 0:
    x = float(input("Introduce un número (0 para terminar): "))
    if x != 0:
        suma += x
        contador += 1
media = suma / contador if contador > 0 else 0
print("Suma:", suma)
print("Media:", media)
