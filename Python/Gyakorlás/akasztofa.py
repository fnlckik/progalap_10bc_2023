from random import randrange
from os import system

# Kap egy "s" szöveg paramétert
# kirajzolja a neki megfelelő feladványt
# (az aktuális állapotot)
def kirajzol(s):
    print("Feladvány:")
    for i in range(len(s)):
        print(s[i], end=" ")
    print()

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

def main():
    system("cls")
    megoldas = sorsolas()
    aktualis = kezdeti_allapot(len(megoldas))
    print(megoldas) # csalás magunknak
    kirajzol(aktualis)
    betu = input("\nBetű: ")
    csere(betu, aktualis, megoldas)
    kirajzol(aktualis)

main()