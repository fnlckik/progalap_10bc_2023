# Csináljunk egy akasztófa játékot!
from random import randrange

def sorsolas():
    szavak = [
        "krumplistészta", "algéria",
        "prímfaktorizáció", "oroszlánszívű",
        "nem", "monitor",
        "microsoft"
    ]
    r = randrange(len(szavak))
    return szavak[r]

# Eldönti, hogy c1 és c2 karakterekből képzett szó
# benne van-e a listában!
# Pl.: "c", "s" => True
# Pl.: "t", "x" => False
def eleme(c1, c2, lista):
    ...

def kiiras(szo):
    # print("_ "*len(szo))
    ketjegyuek = ["cs", "dz", "gy", "ly", "ny", "sz", "ty", "zs"]
    for i in range(len(szo)):
        if eleme(szo[i], szo[i+1], ketjegyuek):
            print("__ ", end="")
        else:
            print("_ ", end="")
    print()

def main():
    megoldas = sorsolas()
    kiiras(megoldas)

main()