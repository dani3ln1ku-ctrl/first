# game.py
"""
Ära arvamise mäng. Mõeldud numbrid on 1-100
Loetakse samme. Mängul on tagauks (1000)
Täidendus: mängu lõppedes küsi kasutajalt mangu veel mangida?
Kui jah (J, j), siis rseti andmed ja alusta uut mängu
1. Kuhu kirjutada, mida kirjutada, kas teha funktsioon?
"""
from random import randint
pc_nr = randint(1, 100)
steps = 0 # sammud lugeja
game_over = False # KAS MANG ON LÄBI


#print(pc_nr) # test

def ask():
    global steps, game_over # Globaalsed muutujad
    user_nr = int(input("Sisesta number: "))
    steps += 1 # Sammud kasvavd +1

    if user_nr > pc_nr and user_nr != 1000:
        print("Väiksem")
    elif user_nr < pc_nr and user_nr != 1000:
        print("Suurem")
    elif user_nr == pc_nr and user_nr != 1000:
        game_over = True
        print(f"Arvasid numbri ära {steps} sammuga.")
    elif user_nr == 1000:
        print(f"leidsid mu nõrga koha. Number on {pc_nr}")

def lest_play():
    global pc_nr, steps, game_over
    while not game_over:
        ask()
    result = input("Kas mängime veel? [J/E]")
    if result == "J" or result == "j":
        pc_nr = randint(1, 100)
        steps = 0
        game_over = False
        lest_play()

lest_play()


