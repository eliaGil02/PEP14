"""
Escribe un programa en Python que lea por teclado una cadena y un carácter, y
reemplace todos los dígitos en la cadena por el carácter. Ej: su clave es: 1540 y X debería
devolver su clave es: XXXX
"""

# leer datos por teclado
cadena = input("Introduce una cadena: ")
caracter = input("Introduce un caracter: ")

# reemplazar los digitos por el caracter
resultado = ""

for c in cadena:
    if "0" <= c <= "9":
        resultado += caracter
    else:
        resultado += c

print(resultado)
