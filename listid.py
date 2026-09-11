# listid
# List ehk massiiv
# List [ nimikiri,loend], tuple (järjend), dictionary {sõnastik}

places = [] # Loo tühi list
places.append("Kehtna")# Lisa uus koht listi lõppu
places.append("Rapla")
places[1:1] = ["Tallinn", "Pärnu"] # Lisa Kehtna ja Rapla vahele
places.extend(["Viljandi", "Tartu", "Rapla"]) # Lisa lõppu
places.insert(2, "Are")

numbers = [1, 7, 4, 25, -35]


print(places)# Näita kohanimede listi
print(numbers)# Näita numbrite listi
print(type(places))# näita kohanimede muutuja tüüpi

# Kustutamine
places.remove("Rapla")# Esimene eemaldatakse
places.pop(6) # Viimane Rapla
del places[2] # kustutab Are

#Ülesaane: Lisa Rapla,Pärnu ja Vilandi vahele ning listi lõppu
places.append("Rapla")
places.insert(3, "Rapla")
# Leimame alemendi indeks ja mitu korda esineb (Rapla)
place = places[-1] # Nimikirja viimane Rapla
index = places.index(place)# Mis indeks on esimene Rapla
count = places.count(place)


print(places, index, count)

if place in places:
    print(f"{place} on nimekirjas olemas.")
    
if "Kohila" in places:
    print(f"Kohila on nimekirjas olemas.")# Seda ride ei vastuseese ei tule

print(len(places)) # Listi suurus
print(places[len(places)-1])# Viimane element listist (Rapla)

# Koopia listist
list_copy = places.copy()
list_list = list(places)

# Sorteerimine
list_copy.sort()
new_list_list = sorted(places, reverse=True) # Z->A

print(list_copy)# Sorteeritud
print(new_list_list) # Z->A
print(places)# Original

print() # tühi rida

# Tühjenda list
new_list_list.clear()

print(new_list_list)
"""
Ül: kasuta originaal listi a eemalda listist viimane Rapla
ilma [-1] kasutama. Väljasta kolmanda elemendi keskmine täht
SUURTÄHENA
"""

places.pop(len(places)-1) # Eemalda lisati viimane Rapla
print(places) # Kontrolli eelmise rea tulemsust
print(laces[2][2].title()) # Pärnu => R


