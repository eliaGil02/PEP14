"""
Escribe un programa en Python que lea por teclado números y los guare en una lista, el
proceso finaliza cuando se introduzca un número negativo. A continuación que muestre el
máximo de los números guardado en la lista y los números pares de la lista.
"""

numeros = []

# leer numeros hasta un negativo
num = int(input("Introduce un número: "))

while num >= 0:
    numeros.append(num)
    num = int(input("Introduce un número: "))

if numeros:
    # max de la lista
    print(max(numeros))

    # pares
    for n in numeros:
        if n % 2 == 0:
            print(n, end=" ")

else:
    print("No hay números válidos")
