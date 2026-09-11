# funktsioonid.py
def welcome():
    print("Tere, kuidas läheb?")


def welcome_name(name):
    return f"Tere, {name}!"


def divison(number1, number2):
    """Teostab kahe arvu jagamist"""
    if number2 !=0:
        return number1 / number2
    return -1 # See on viga ehk 0 jagamine


def introduce(name, age=20):
    """
    loob lihtsa tutvustava lause

    :param name: str isiku nimi
    :param age: int isiku vanus (vaikimisi 20)
    :return: tekstiline tutvstav lause
    :rtype: string

    """
    return f"Tema on {name} ja ta on {age} aastane!"



welcome()
for x in range(3):
    welcome()

print() # tühi rida

print(welcome_name("Daniel"))
names = ["Juhan", "Mari", "Margus"]
for name in names:
    print(welcome_name(name))
print(welcome_name(1234)) # Tere, 1234!
print(welcome_name("")) # Tere, !
print() # tühi rida


print(divison(4, 2))
print(divison(10, 0))

print(introduce("Daniel", 16))
print(introduce(age=99, name="Vanaema"))
print(introduce(1234, 56))

print(divison(numbers2=10, number1=100))
