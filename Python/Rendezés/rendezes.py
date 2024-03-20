from random import randint
from time import time

# Eljárás:
# Megcseréli az "x" lista
# "i"-edik és "j"-edik elemét!
def csere(x, i, j):
    # seged = x[i]
    # x[i] = x[j]
    # x[j] = seged
    x[i], x[j] = x[j], x[i]

# Függvény:
# Az "x" listában a "k"-adik elemtől
# kezdve melyik a legkisebb indexű?
def minindex(x, k):
    index = k
    for i in range(k+1, len(x)):
        if x[i] < x[index]:
            index = i
    return index

# Minimumkiválasztásos rendezés
# Mj: ez pontosan n darab cserét végez
# 1. Megkeressük az i-edik legkisebb elemet
# 2. Megcseréljük az aktuálissal
def minkiv(x):
    for i in range(len(x)):
        j = minindex(x, i)
        csere(x, i, j)

# Buborékos rendezés
# Mj: Nem fix számú cserét végez
# 1. Csak egymás melletti elemeket cserélünk!
# 2. Megállunk ha nem volt több csere
def buborek(x):
    n = len(x)
    for i in range(n):
        vanCsere = False
        for j in range(n-i-1):
            if x[j] > x[j+1]:
                csere(x, j, j+1)
                vanCsere = True
        if not vanCsere:
            return

# Függvény:
# Megad egy "n" elemű listát
# 1 és 9 közötti random
# számokkal feltöltve!
def feltolt(n):
    eredmeny = []
    for i in range(n):
        r = randint(1, 9)
        eredmeny.append(r)
    return eredmeny

# Másolás tétele
def masol(x):
    masolat = []
    for i in range(len(x)):
        masolat.append(x[i])
    return masolat

# 5 6 7 8 7 8 9 8 7 8 9 10 11 12 11 12 13
# 80%-ban az előzőnél 1-gyel nagyobb
# 20%-ban az előzőnél 1-gyel kisebb
def feltolt_nagyjabol_rendezett(n):
    eredmeny = []
    eredmeny.append(randint(1, 9))
    for i in range(n):
        elozo = eredmeny[i]
        r = randint(1, 10)
        if r <= 8:
            eredmeny.append(elozo + 1)
        else:
            eredmeny.append(elozo - 1)          
    return eredmeny

def teszt(n):
    x = feltolt(n)
    print("Lista feltöltve!")
    
    y = x.copy()
    kezdet = time()
    minkiv(y)
    veg = time()
    print("Minkiv kész:", veg - kezdet)
    
    z = x.copy()
    kezdet = time()
    buborek(z)
    veg = time()
    print("Buborékos kész:", veg - kezdet)
    
    kezdet = time()
    w = sorted(x)
    veg = time()
    print("Gyors rendezés:", veg - kezdet)

def main():
    # x = [5, 2, 7, 1, 2, 3]
    # print("Eredeti:", x)
    # minkiv(x)
    # print("Rendezett:", x)

    # x = feltolt(100)
    # print("Random lista:", x)
    # minkiv(x)
    # print("Rendezett random:", x)
    teszt(100)

main()