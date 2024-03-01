from random import randrange
from os import system

# Kap egy "s" szöveg paramétert
# kirajzolja a neki megfelelő feladványt
def vonalak_kirajzol(s):
    print("Feladvány:")
    for i in range(len(s)):
        print("_", end=" ")
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

def main():
    system("cls")
    megoldas = sorsolas()
    print(megoldas)
    vonalak_kirajzol(megoldas)

main()