"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
Declara una cadena " Hola Mundo ".
Aplica y muestra los resultados de: upper(), lower(), capitalize(), title().
Elimina espacios con strip().
Sustituye "Mundo" por "Python" con replace().
Divide la cadena en palabras con split().
Une una lista de palabras con join().
"""

# declarar la cadena
cadena = " Hola Mundo "

# aplicar metodos de cadena
print(cadena.upper())
print(cadena.lower())
print(cadena.capitalize())
print(cadena.title())

# eliminar espacios
cadena_sin_espacios = cadena.strip()
print(cadena_sin_espacios)

# sustituir "mundo" por "python"
cadena_reemplazada = cadena_sin_espacios.replace("Mundo", "Python")
print(cadena_reemplazada)

# dividir la cadena
lista_palabras = cadena_sin_espacios.split()
print(lista_palabras)

# unir una lista de palabras
cadena_unida = " ".join(lista_palabras)
print(cadena_unida)
