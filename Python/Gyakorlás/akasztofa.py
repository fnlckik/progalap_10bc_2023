from random import randrange
from os import system

# Eljárás:
# Kap egy "s" szöveg paramétert
# kirajzolja a neki megfelelő feladványt
# (az aktuális állapotot)
def kirajzol(s):
    print("Feladvány:")
    for i in range(len(s)):
        print(s[i], end=" ")
    print()

# Függvény:
# Egy listából választ egy random
# szót és visszaadja
def sorsolas():
    szavak = [
        "hálózat", "python", 
        "számítógép", "értelmes", 
        "szavak", "dolgozat"
    ]
    r = randrange(len(szavak))
    neo = szavak[r]
    return neo

# Függvény:
# Állapottér
# Előállít egy megoldás hosszú listát
# "_" karakterekkel!
def kezdeti_allapot(n):
    eredmeny = []
    for i in range(n):
        eredmeny.append("_")
    return eredmeny

# Eljárás:
# Kicseréli a "megoldas" szerint eltalált
# "betu"-ket az "aktualis" listában!
def csere(betu, aktualis, megoldas):
    for i in range(len(megoldas)):
        if megoldas[i] == betu:
            aktualis[i] = betu

# Függvény:
# Benne van-e "elem" a "lista"-ban?
# (True, False)
def bennevan(elem, lista):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)

# Függvény:
# Egy forduló lebonyolítása
# Megadja, hogy a forduló után
# hány hibánál járunk.
# Early return: korai visszatérés (hibás esetek kezelése)
def fordulo(aktualis, megoldas, rosszak):
    betu = input("\nBetű: ")
    if len(betu) > 1:
        return len(rosszak)
    if not bennevan(betu, megoldas) and not bennevan(betu, rosszak):
        rosszak.append(betu)
    csere(betu, aktualis, megoldas)
    system("cls")
    print(megoldas) # csalás magunknak
    print("Hibák száma:", len(rosszak))
    print("Rosszak:", rosszak)
    kirajzol(aktualis)
    return len(rosszak)

def eredmenyhirdetes(hibaszam):
    print()
    if hibaszam <= 2:
        print("Nyertél!")
    else:
        print("Vesztettél!")

# Eljárás:
# Egy teljes játék lebonyolítása
# Vége: nyereség vagy veszteség
def jatek(megoldas):
    aktualis = kezdeti_allapot(len(megoldas))
    kirajzol(aktualis)
    rosszak = []
    while bennevan("_", aktualis) and len(rosszak) <= 2:
        fordulo(aktualis, megoldas, rosszak)
    eredmenyhirdetes(len(rosszak))

def main():
    system("cls")
    megoldas = sorsolas()
    print(megoldas) # csalás magunknak
    jatek(megoldas)

main()