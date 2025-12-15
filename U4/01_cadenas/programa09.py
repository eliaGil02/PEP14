"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
Muestra el código Unicode de un emoji (ord(), hex()).
Crea un carácter a partir de un código numérico (chr()).
Imprime los caracteres ASCII del 48 al 57 (dígitos) en una línea.
"""

# mostrar el codigo Unicode de un emoji
emoji = "😀"
codigo = ord(emoji)

print("codigo unicode:", codigo)
print("codigo unicode en hexadecimal:", hex(codigo))

# crear un caracter a partir de un codigo numerico
codigo_num = 65
caracter = chr(codigo_num)
print("caracter creado:", caracter)

# imprimir los caracteres ASCII del 48 al 57
for i in range(48, 58):
    print(chr(i), end=" ")
