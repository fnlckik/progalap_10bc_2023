# Csináljunk egy akasztófa játékot!
from random import randrange
from os import system

# Függvény:
# Választ egy véletlen szót
# egy konstans listából!
def sorsolas():
    szavak = [
        "krumplistészta", "algéria",
        "prímfaktorizáció", "oroszlánszívű",
        "nem", "monitor",
        "microsoft"
    ]
    # szavak = ["szőlő", "kutya", "macska", "szivárvány", "nyuszi"]
    # szavak = ["tyúkszárny"]
    # szavak = ["egészség"]
    # szavak = ["rézszék"]
    r = randrange(len(szavak))
    return szavak[r]

# Függvény:
# Eldönti, hogy c1 és c2 karakterekből képzett szó
# benne van-e a listában!
# Pl.: "c", "s" => True
# Pl.: "t", "x" => False
def eleme(c1, c2, lista):
    szo = c1 + c2
    i = 0
    while i < len(lista) and not(szo == lista[i]):
        i += 1
    return i < len(lista)
    # if i < len(lista):
    #     return True
    # else:
    #     return False

# Eljárás:
# Kiírja a kapott lista elemeit
# figyelve (viszonylag) a kétjegyű
# mássalhangzókra.
def kiiras(aktualis, megoldas):
    # print("_ "*len(szo))
    print("Feladvány:")
    ketjegyuek = ["cs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]
    ketjegyuE = False
    i = 0
    while i < len(aktualis) - 1:
        ketjegyuE = eleme(megoldas[i], megoldas[i+1], ketjegyuek)
        if ketjegyuE:
            print(f"{aktualis[i]}{aktualis[i+1]} ", end="")
            i += 2
        else:
            print(f"{aktualis[i]} ", end="")
            i += 1
    if not ketjegyuE:
        print(aktualis[i])
    else:
        print()

# Függvény:
# Előállítja a megoldas hosszával
# egyenlő hosszú, alulvonásokat ("_")
# tartalmazó listát
def kezdeti_allas(megoldas):
    lista = []
    for i in range(len(megoldas)):
        lista.append("_")
    return lista

# Függvény:
# Megnézi, hogy a megoldas melyik
# karakterei egyeznek a betu-vel
# és az aktualis lista megfelelő
# elemeit lecseréli a betűre.
# Visszatérési érték: Hány csere volt?
def csere(aktualis: list[str], betu: str, megoldas: str):
    db = 0
    for i in range(len(megoldas)):
        if megoldas[i] == betu:
            aktualis[i] = betu
            db += 1
    return db
# Példa:
# megoldas = "alma"
# betu = "m"
# aktualis = ["_", "_", "_", "_"]
# Ekkor => aktualis = ["_", "_", "m", "_"]

# Függvény:
# Beolvasunk egy betűt a felhasználótól
# és cseréljük a lista megfelelői
# elemeit a helyes betűre!
# Visszatérés: Hány találatos volt a tipp?
def tipp(aktualis, megoldas):
    betu = input("Tipp: ")
    db = csere(aktualis, betu, megoldas)
    return db

# Függvény:
# Egy lista karaktereit
# szöveggé fűzi össze.
def szoveg(lista):
    s = ""
    for i in range(len(lista)):
        s += lista[i]
    return s
# Pl.: szoveg(["a", "l", "m", "a"]) == "alma"

# Eljárás:
# Játék ciklus
# Ez történik a játék során.
def jatek(aktualis, megoldas):
    hibak_szama = 0
    while szoveg(aktualis) != megoldas and hibak_szama < 10:
        eltalalt = tipp(aktualis, megoldas)
        if eltalalt == 0:
            hibak_szama += 1
        system("cls")
        print("Hibák száma:", hibak_szama)
        kiiras(aktualis, megoldas)
    if hibak_szama < 10:
        print("Nyertél!")
    else:
        print("Vesztettél!")

def main():
    system("cls")
    megoldas = sorsolas()
    print(megoldas) # csalás magunk számára
    aktualis = kezdeti_allas(megoldas)
    kiiras(aktualis, megoldas)
    jatek(aktualis, megoldas)
    
main()