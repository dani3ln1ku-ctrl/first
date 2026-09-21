import math

a = int(input("Sisesta arv a: "))

print(a)

b = int(input("Sisesta arv b: "))

print(b)
 
pindala = a * b
Ümbermõõt = 2 * (a+b)
diagonaal = math.sqrt(a**2 + b**2)

print("Pindala:", pindala, "cm²")
print("Ümbermõõt:", Ümbermõõt, "cm")
print("Diagonaal:", round(diagonaal, 2), "cm")