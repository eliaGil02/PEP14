"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuanto deberá pagar finalmente por su compra.
"""

totalCompra = float(input("Introduce el total de la compra: "))

dto = totalCompra * 0.15
total_final = totalCompra - dto

print("Descuento aplicado: ", dto)
print("Total a pagar: ", total_final)
