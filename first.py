import datetime # Kuupäeva arvutamiseks
# See on kommentaar

"""
Mitme realine
kommentaar
"""

# Muutujate omistamine
name = "daniel nocovnijs"
age = 16
height = 1.7 # Alati punkt!

print(name, age, height)
# Kasutaja NAME vanuses AGE on pikkusega Height meetrit
print(f"Kasutaja {name.title()} vanusega {age}a. on pikkusega {height} meetrit.")
print("Kasutaja " + name.title() + " vanusega " + str(age) + " a. on pikkusega " + str(height) + " meetrit.")

# Jooksev aasta
birth_year = datetime.date.today().year - age
print(f"Sünniaasta: {birth_year}")

age = int(input("Sisesta vanus: "))

if age < 1 or age > 122:
    print("Vanus on vales vahemikus (lubatud 1-122 k.a.)")
elif age < 18:
    print("Alaealine") # 1-17
elif age < 64:
    print("Tööealine") # 18-64
elif age < 100:
    print("Pensionär") # 65-99
else:
    print("Pikaealine") # 100-122
    
"""
Küsime elukoha ja vastavalt elukoha nime pikkusele väljastame
Lühike nimi (2-6 täthe)
Pikk nimi (7- täthe)
"""

place = input("Sisesta elukoht: ")
place = place.strip() # EEmaldab tühikud algusest ja lõpust

if len (place) > 1 and len(place) <= 6 and place.isalpha():
    print(f"Lühike nimi {place}")
elif len(place) > 6 and place.isalpha():
    print(f"Pikk nimi {place}")
else:
    print("Viga!")
    
    
# Substring (alamstingid)
# Muutuj name
print(name)
print(name[1])		#Väljund: a
print(name[1:5])	#Välujund: anie
print(name[6:])		#Väljund: Nocovnijs
print(name[:5])		#Väljund: Danie
print(name[::-1])	#Väljund: sjinvocoN leinaD

# Muutujast name välja perekonnanime esime täht Suurelt

print(name[7].title())# OK

# Kolm andmetüüpi
print("------")
print(type(name))
print(type(age))
print(type(height))