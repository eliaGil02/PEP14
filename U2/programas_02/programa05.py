"""
Escribe un programa que pida un número y muestre una lista de números desde 1 al
número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se
pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto.
"""

while True:
    n = int(input("Introduce un número entre 1 y 10: "))
    if 1 <= n <= 10:
        break
    print("Valor inválido")
for i in range(1, n + 1):
    print(i)
