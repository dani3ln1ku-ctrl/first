from random import randint
names = ["Mari", "Anna", "Villem", "Jüri"] # List

# Väljasta ist olevad nimed nime kaupa
for name in names:
    print(name) # Väljasta nimi

print() # tühi rida

# Sama lahendus nagu enne, aga lisaks juhuslik vanus
for x in range(len(names)):
    print(x, names[x], randint(1, 122))

print()

for x in range(1, 5): #
    print(x, end=" ") # Ei tee Reavahetust
print("\n")# Reavahetus + tühi rida

for x in range(0, 10, 2):
    print(x, end=" | ")
print("\n") # Reavahetus + rida

# while-loop
x = 0
while x < len(names):
    print(names[x])
    x += 1

# ÜL: väljasta listi nimed konsooli ja iga nime ette 
#pane järjekorra number koos punktiga. Seega:
# 1. mari
# 2. anna
# .....

for x in range(len(names)):
    print(f"{1+x}. {names[x]}")