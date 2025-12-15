"""
Mejora las funciones anteriores de cifrado y descifrado con los siguientes cambios.
• El cifrado César original cambia cada carácter por otro: a se convierte en b, z se
convierte en a, y así sucesivamente (por defecto el valor desplazado es 1). Ahora
la idea es hacerlo un poco más difícil y permitir que el valor desplazado provenga
del rango 1 – 25 (si valor de desplazado es 3, la A se cambiará por la D).
• Además, deja que el código conserve las mayúsculas y minúsculas (las minúsculas
permanecerán en minúsculas) y todos los caracteres no alfabéticos deben
permanecer intactos.
Escribe un programa que:
• Le pida al usuario una línea de texto para cifrar..
• Le pida al usuario un valor de cambio (un número entero del rango 1..25, nota:
debes validar la entrada para asegurarnos que el número está dentro del rango).
• Imprima el texto cifrado.
"""


def cifrar_cesar(texto, desplazamiento):
    resultado = ""

    for c in texto:
        if c.isalpha():
            if c.isupper():
                base = ord("A")
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
            else:
                base = ord("a")
                resultado += chr((ord(c) - base + desplazamiento) % 26 + base)
        else:
            resultado += c

    return resultado


def descifrar_cesar(texto, desplazamiento):
    return cifrar_cesar(texto, -desplazamiento)


texto = input("Introduce el texto a cifrar: ")

desplazamiento = 0
valido = False

while not valido:
    desplazamiento = int(input("Introduce el valor de desplazamiento entre 1 y 25: "))
    if 1 <= desplazamiento <= 25:
        valido = True
    else:
        print("El valor debe estar entre 1 y 25")

texto_cifrado = cifrar_cesar(texto, desplazamiento)

print(texto_cifrado)
