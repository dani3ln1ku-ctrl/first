# read csv v1

filename = "Create-MyCSV-v.csv"
row = 2 # Mitmes veerg kokku liita
total = 0 # Kogu veeru summa

f = open(filename, "r" ) # ava file lugemiseks
content = f.readlines()

f.close() # sule file

for line in content:
    line = line.strip() # korrasta rida (eemalda \n)
    parts = line.split(";")
    if parts[row].isnumeric():
        total += int(parts[row])
        #print(line)


print(total)