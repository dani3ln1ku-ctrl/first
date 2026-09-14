# read csv v2
"""
Täiendus: loenda kokku mitu numbrit kokku liidetakse.
näita ka vastust.



"""
filename = "Create-MyCSV-s.csv"
#row = 2 # Mitmes veerg kokku liita
total = 0 # Kogu veeru summa
count = 0
# loe kokku mitu veergu on failis

f = open(filename, "r" ) # ava file lugemiseks
rows = len(f.readline().split(";")) # Mitu elementi reas
f.close # sule file

row = int(input(f"Mitmes veerg kokku liita? 1-{rows} "))

if row >= 1 and row <= rows:
    row -= 1 # row = row -1
    with open(filename, "r") as f:
        content = f.readlines()
        for line in content:
            line = line.strip() # korrasta rida (eemalda \n)
            parts = line.split(";")
            if parts[row].isnumeric():
                total += int(parts[row])
                count += 1 # kasvab ühe võrra
        
    print(count, total) 

else:
    print("Vigane veeru number!")
















