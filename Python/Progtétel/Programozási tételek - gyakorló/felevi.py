#F1
n = int(input())
nevek, magyar, matek, tori = [], [], [], []
for i in range(n):
    sor = input().split()
    nevek.append(sor[0])
    magyar.append(int(sor[1]))
    matek.append(int(sor[2]))
    tori.append(int(sor[3]))
print(tori)

#F2 - Összegzés (átlag)
print("2. feladat:", end=" ")
osszeg = 0
for i in range(n):
    osszeg += tori[i]
atlag = osszeg / n
print(round(atlag, 3))

#F3 - Megszámolás
print("3. feladat:", end=" ")
db = 0
for i in range(n):
    if matek[i] == 1:
        db += 1
print(db)

#F4 - Maximum-kiválasztás
print("4. feladat:", end=" ")
maxi = 0
maxe = (magyar[0] + matek[0] + tori[0]) / 3
for i in range(1, n):
    atlag = (magyar[i] + matek[i] + tori[i]) / 3
    if atlag > maxe:
        maxi = i
        maxe = atlag
print(nevek[maxi])

#F5 - Keresés
print("5. feladat:", end=" ")
i = 0
while i < n and not(matek[i] > magyar[i]):
    i += 1
if i < n:
    print(nevek[i])
else:
    print("Nincs")

# F6 - Kiválogatás
print("6. feladat:", end=" ")
diakok = []
for i in range(n):
    nev = nevek[i] # Oliver
    hossz = len(nev) # 6 -> 5 az utso karakter
    if nev[hossz-1] == "a":
        diakok.append(nevek[i])
print(len(diakok), end=" ")
for i in range(len(diakok)):
    print(diakok[i], end=" ")
print()

# F7 - Eldöntés
print("7. feladat:", end=" ")
i = 0
while i < n and not(magyar[i] == matek[i] and matek[i] == tori[i]):
    i += 1
if i < n:
    print("Van")
else:
    print("Nincs")

# F8
print("8. feladat:", end=" ")
mini = -1
mine = 5000
for i in range(n):
    if magyar[i] == 5 and matek[i] <= mine:
        mini = i
        mine = matek[i]
if mine == 5000:
    print(-1)
else:
    print(nevek[mini])

# F9
print("9. feladat:", end=" ")


# F10
print("10. feladat:", end=" ")

