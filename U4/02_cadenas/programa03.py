"""
Escribe un programa en Python que lea una cadena de caracteres y muestre la siguiente
información:
• La primera letra de cada palabra escrita en mayúsculas. Por ejemplo, si recibe
Organización de las Naciones Unidas, debe devolver ONU.
• Las palabras que comienzan por minúscula. Por ejemplo, si recibe
Organización de las Naciones Unidas, debe devolver de y las.
"""

# leer la cadena
cadena = input("Introduce una cadena: ")

# separa la cadena en palabras
palabras = cadena.split()

# obtener las iniciales en mayus
siglas = ""
for palabra in palabras:
    siglas += palabra[0].upper()

print("Siglas:", siglas)

# mostrar las palabras que empiecen por minus
for palabra in palabras:
    if palabra[0].islower():
        print(palabra)
