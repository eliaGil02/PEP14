"""
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
"""

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
anio = int(input("Introduce el año: "))

fechaValida = True

if mes < 1 or mes > 12:
    fechaValida = False
elif dia < 1:
    fechaValida = False
elif mes in [1, 3, 5, 7, 8, 10, 12] and dia > 31:
    fechaValida = False
elif mes in [4, 6, 9, 11] and dia > 30:
    fechaValida = False
elif mes == 2:
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        if dia > 29:
            fechaValida = False
    else:
        if dia > 28:
            fechaValida = False

if fechaValida:
    print("Correcto")
else:
    print("Incorrecto")
