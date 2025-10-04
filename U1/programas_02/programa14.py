"""
Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos
GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.

La salida debe ser algo así:
1000000000 bytes en sistema decimal (SI): 1 GB, 0 MB, 0 KB, 0 bytes
1000000000 bytes en sistema binario (IEC): 0 GiB, 953 MiB, 690 KiB, 512 bytes
Unidad Sistema decimal (SI) Sistema binario (IEC)
1 KB / KiB 1.000 bytes 1.024 bytes
1 MB / MiB 1.000 KB 1.024 KiB
1 GB / GiB 1.000 MB 1.024 MiB
1 TB / TiB 1.000 GB 1.024 GiB
1 PB / PiB 1.000 TB 1.024 TiB
1 EB / EiB 1.000 PB 1.024 PiB
 Decimal (SI, 1000) → lo usan fabricantes de discos, redes, marketing de
almacenamiento.
 Binario (IEC, 1024) → lo usan sistemas operativos, memoria RAM, tamaños de
archivos.
"""

bytesInput = int(input("Introduce la cantidad de bytes: "))

gbSI = bytesInput // 1_000_000_000
mbSI = (bytesInput % 1_000_000_000) // 1_000_000
kbSI = (bytesInput % 1_000_000) // 1_000
bSI = bytesInput % 1_000

gibIEC = bytesInput // (1024**3)
mibIEC = (bytesInput % (1024**3)) // (1024**2)
kibIEC = (bytesInput % (1024**2)) // 1024
bIEC = bytesInput % 1024

print(
    f"{bytesInput} bytes en sistema decimal (SI): {gbSI} GB, {mbSI} MB, {kbSI} KB, {bSI} bytes"
)
print(
    f"{bytesInput} bytes en sistema binario (IEC): {gibIEC} GiB, {mibIEC} MiB, {kibIEC} KiB, {bIEC} bytes"
)
