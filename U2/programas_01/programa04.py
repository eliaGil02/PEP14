"""
Escribe un programa que lea por teclado un número real entre 1 y 10, simulando una
nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en
cuenta los siguientes rangos:
• Insuficiente: [0, 5)
• Suficiente: [5, 6)
• Bien: [6, 7)
• Notable: [7, 9)
• Sobresaliente: [9, 10]
"""

nota = float(input("Introduce una nota entre 0 y 10: "))

if nota < 0 or nota > 10:
    print("Aviso: la nota debe estar entre 0 y 10")
elif nota < 5:
    print("Calificación: Insuficiente")
elif nota < 6:
    print("Calificación: Suficiente")
elif nota < 7:
    print("Calificación: Bien")
elif nota < 9:
    print("Calificación: Notable")
else:
    print("Calificación: Sobresaliente")
