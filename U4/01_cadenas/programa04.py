"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
 Convierte un número entero, un número decimal y un booleano en cadenas(str()).
 Convierte una cadena en entero y en decimal (int(), float()).
 Crea una cadena cruda (r"...") que contenga caracteres especiales y muéstrala.
"""

# conversion de distintos tipos de cadenas
num_entero = 10
num_decimal = 3.14
valor_bool = True

print(str(num_entero))
print(str(num_decimal))
print(str(valor_bool))

# conversion de cadena a entero y decimal
cadena_num = "25"
print(int(cadena_num))
print(float(cadena_num))

cadena_cruda = r"Hola\gjsfjg\igdagnjdn\hola"
print(cadena_cruda)
