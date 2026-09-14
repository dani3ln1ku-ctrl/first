from math import pi, pow

radius = float(input("Sisesta ringi raadius: ")) # float on komadega arvutamine

if radius <1 or radius > 10:
    print("Raadius vales vahemikus.")
else:
    P = 2 * pi * radius # ümbermõõt
    A = 2 * pi * pow(radius, 2) # pindala
    print(f"Raadius: {radius}")
    print(f"Ümbermõõt: {P}")
    print(f"Pindala: {A}")

