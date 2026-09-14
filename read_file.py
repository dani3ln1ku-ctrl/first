# read_file.py
"""
Täindus : Näita ainult neidisikuid kes on 100 ja rohkem vanad.

"""
filename = "create_file.txt"

with open(filename, "r", encoding="utf-8") as f:
    contents = f.readlines() # Loe kõik read listi
    for line in contents:
        line = line.strip() # korrasta rida
        name = line.split(";")[0]
        age = int(line.split(";")[1]) # teeb täiskarvuks , muidu string
        if age  >= 100:
            print(name, age)
        #print(type(name), type(age)) # näita nime ja vanuse tüüpi (str, int)
        datetime = 2026 - age
       print(datetime)
        