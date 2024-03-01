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
def kiirasa(szo):
    # print("_ "*len(szo))
    print("Feladvány:")
    ketjegyuek = ["cs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]
    ketjegyuE = False
    i = 0
    while i < len(szo) - 1:
        ketjegyuE = eleme(szo[i], szo[i+1], ketjegyuek)
        if ketjegyuE:
            print(f"{szo[i]}{szo[i+1]} ", end="")
            i += 2
        else:
            print(f"{szo[i]} ", end="")
            i += 1
    if not ketjegyuE:
        print(szo[i])
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

# Eljárás:
# Megnézi, hogy a megoldas melyik
# karakterei egyeznek a betu-vel
# és az aktualis lista megfelelő
# elemeit lecseréli a betűre.
def csere(aktualis: list[str], betu: str, megoldas: str):
    for i in range(len(megoldas)):
        if megoldas[i] == betu:
            aktualis[i] = betu
# Példa:
# megoldas = "alma"
# betu = "m"
# aktualis = ["_", "_", "_", "_"]
# Ekkor => aktualis = ["_", "_", "m", "_"]

# Eljárás:
# Beolvasunk egy betűt a felhasználótól
# és cseréljük a lista megfelelői
# elemeit a helyes betűre!
def tipp(aktualis, megoldas):
    betu = input("Tipp: ")
    csere(aktualis, betu, megoldas)

def main():
    system("cls")
    megoldas = sorsolas()
    print(megoldas) # csalás magunk számára
    aktualis = kezdeti_allas(megoldas)
    kiirasa(aktualis)
    while True:
        tipp(aktualis, megoldas)
        kiirasa(aktualis)

main()