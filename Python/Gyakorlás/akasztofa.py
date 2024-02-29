# Csináljunk egy akasztófa játékot!
from random import randrange

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

def kiiras(szo):
    # print("_ "*len(szo))
    ketjegyuek = ["cs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]
    ketjegyuE = False
    i = 0
    while i < len(szo) - 1:
        ketjegyuE = eleme(szo[i], szo[i+1], ketjegyuek)
        if ketjegyuE:
            print("__ ", end="")
            i += 2
        else:
            print("_ ", end="")
            i += 1
    if not ketjegyuE:
        print("_")
    else:
        print()

def main():
    megoldas = sorsolas()
    print(megoldas)
    kiiras(megoldas)

main()