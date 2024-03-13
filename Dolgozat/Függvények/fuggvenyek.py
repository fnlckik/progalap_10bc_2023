from random import randint

# F1
def atlag(a, b):
    return (a + b) / 2

# F2
def csere(lista, ertek=""):
    r = randint(0, len(lista)-1)
    lista[r] = ertek

# F3
# 1:2:3 => 6
def betusor(a, b, c):
    s = ""
    for i in range(30):
        r = randint(1, 6)
        if r == 1:
            s += a
        elif r == 2 or r == 3:
            s += b
        else:
            s += c    
    return s

# F4
def bennevan(elem, lista):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)

def pozitivak(lista):
    eredmeny = []
    for i in range(len(lista)):
        if lista[i] > 0 and not bennevan(lista[i], eredmeny):
            eredmeny.append(lista[i])
    return eredmeny


# F5
# Van-e ennél hidegebb bolygó?
# -142 141 251
def maximum(lista):
    maxe = lista[0]
    for i in range(len(lista)):
        if lista[i] > maxe:
            maxe = lista[i]
    return maxe

def nagyobbak_szama(lista1, lista2):
    if lista1 == []:
        return len(lista2)
    m = maximum(lista1)
    db = 0
    for i in range(len(lista2)):
        if lista2[i] > m:
            db += 1
    return db

# F6 - Bónusz
# 2-től 12-ig
def kockak():
    # gyakorisagok[i]: az (i+2) értékből mennyi volt
    gyakorisagok = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1000):
        r1 = randint(1, 6)
        r2 = randint(1, 6)
        s = r1 + r2
        gyakorisagok[s-2] += 1
    print("6. Gyakoriságok:")
    for i in range(11):
        print(f"   {i+2} => {gyakorisagok[i]}")

# ------------------------------------------------------------

def main():
    # F1
    print("1. Átlag:", atlag(5, 9))

    # F2
    x = ["alma", "korte", "barack", "szilva"]
    csere(x, 404)
    print("2. Csere:", x)

    # F3
    print("3. Betűsor:", betusor("?", "x", "5"))

    # F4
    szamok = [4, -1, 2, -4, -1, 2, 4, 2, 2, 7]
    print("4. Pozitívak:", pozitivak(szamok))

    # F5
    lista1 = [4, 6, 1, 6, 7, 2, 7, 2]
    lista2 = [1, 7, 4, 8, 12, 67, -1, 9, 26]
    print("5. Nagyobbak száma:", nagyobbak_szama(lista1, lista2))

    # F6 - Bónusz
    kockak()

main()