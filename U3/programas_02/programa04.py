"""
El módulo turtle es una biblioteca estándar de Python que permite crear gráficos y dibujos
de manera sencilla, moviendo una “tortuga” virtual por la pantalla. El módulo está instalado
por defecto en el interprete de Python.
Investiga la documentación del módulo https://docs.python.org/3/library/turtle.html y
escribe un programa que:
• Dibuje un cuadrado rojo sin rellenar.
• Dibuje un circulo verde relleno.
"""

import turtle

# Cuadrado rojo sin rellenar
turtle.color("red")
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

# Círculo verde relleno
turtle.penup()
turtle.goto(150, 0)
turtle.pendown()
turtle.color("green", "green")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.done()
