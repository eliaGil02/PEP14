"""
Escribe un programa que
 Cree una variable que almacene el número entero 6.
 Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto
al que apunta la variable (deben ser iguales)
 Cree otra variable a la que se asigne la primera variable.
 Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto
al que apunta la variable (deben ser iguales)
 Utilice los operadores de identidad (is e is not) para comprobar y mostrar por
pantalla que los dos variables apuntan al mismo objeto y por lo tanto a la misma
posición de memoria.
 Asigne la cadena “Hola” a la primera variable.
 Muestre por pantalla el tipo del objeto que contiene la cadena “Hola” y el tipo del
objeto al que apunta la variable (deben ser iguales) (y diferentes al objeto 6).
 Utilice la función isinstance() para comprobar y mostrar por pantalla que el
objeto al que apunta la primera variable es de tipo int y el de la segunda es de
tipo str.
"""

variable1 = 6
print("Variable 1:", variable1, "| Tipo del objeto:", type(variable1))

variable2 = variable1
print("Variable 2:", variable2, "| Tipo:", type(variable2))

print("¿variable1 es variable2?:", variable1 is variable2)
print("¿variable1 no es variable2?:", variable1 is not variable2)

variable1 = "Hola"
print("Nueva variable1:", variable1, "| Tipo:", type(variable1))

print("¿variable1 es int?:", isinstance(variable1, int))
print("¿variable1 es str?:", isinstance(variable1, str))
print("¿variable2 es int?:", isinstance(variable2, int))
print("¿variable2 es str?:", isinstance(variable2, str))
