"""
Escribe un programa en Python que realice las siguientes operaciones con cadenas:
Declara una cadena "programacion en python".
Busca la posición de "python" con find() o index().
Cuenta cuántas veces aparece la letra "o".
Verifica si comienza por "pro" y termina por "on".
"""

# declarar la cadena
cadena = "programacion en python"

# buscar la posicion de python
posicion = cadena.find("python")
print(posicion)

# contar cuantas veces aparece la letra o
contador_o = cadena.count("o")
print(contador_o)

# verificar si comienza por pro
empieza_pro = cadena.startswith("pro")
print(empieza_pro)

# verificar si termina por on
termina_on = cadena.endswith("on")
print(termina_on)
