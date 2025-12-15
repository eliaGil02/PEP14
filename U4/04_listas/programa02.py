"""
Escribe un programa en Python que guarde la temperatura mínima y máxima de 5 días en
una lista de dos dimensiones y a continuación muestre.
• La temperatura media de cada día.
• Los días con menos temperatura.
• Se lea una temperatura por teclado y se muestran los días cuya temperatura
máxima coincide con ella. Si no existe ningún día se muestra un mensaje
de .información
"""

temperaturas = []

# leer las temp min y max de 5d
for dia in range(1, 6):
    min = float(input(f"Introduce la temperatura mínima del día {dia}: "))
    max = float(input(f"Introduce la temperatura máxima del día {dia}: "))
    temperaturas.append([min, max])

# mostrar temperatura media de cada dia
print("\nTemperatura media de cada día:")
for i in range(5):
    media = (temperaturas[i][0] + temperaturas[i][1]) / 2
    print(f"Día {i+1}: {media}")

# dias con menos temperaturas
minima_general = temperaturas[0][0]
for dia in temperaturas:
    if dia[0] < minima_general:
        minima_general = dia[0]
print("\nDías con las temperaturas mínimas mas baja:")
for i in range(5):
    if temperaturas[i][0] == minima_general:
        print(f"Día {i+1}")

# leer una temperatura y mostrar los días cuya máxima coincide
buscar = float(input("\nIntroduce una máxima a buscar: "))
encontrado = False

for i in range(5):
    if temperaturas[i][1] == buscar:
        print(f"Día {i+1}")
        encontrado = True

if not encontrado:
    print("No existe ningún día con esa máxima")
