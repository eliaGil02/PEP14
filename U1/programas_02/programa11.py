"""
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo
de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que
determine la hora de llegada a la ciudad B.
"""

hh = int(input("Introduce la hora de salida (HH): "))
mm = int(input("Introduce los minutos de salida (MM): "))
ss = int(input("Introduce los segundos de salida (SS): "))

n = int(input("Introduce el tiempo de viaje en segundos: "))

totalSalida = hh * 3600 + mm * 60 + ss
totalLlegada = totalSalida + n

hora = (totalLlegada // 3600) % 24
minuto = (totalLlegada % 3600) // 60
segundo = totalLlegada % 60

print(f"Hora de llegada: {hora:02d}:{minuto:02d}:{segundo:02d}")
