#F1
n = int(input())
nevek, magyar, matek, tori = [], [], [], []
for i in range(n):
    sor = input().split()
    nev = sor[0]
    nevek.append(nev)
    x = int(sor[1])
    magyar.append(x)
    x = int(sor[2])
    matek.append(x)
    x = int(sor[3])
    tori.append(x)

#F2
print("2. feladat:", end=" ")
s = 0
for i in range(n):
    s += tori[i]
atlag = s / n
print(round(atlag, 3))

#F3
print("3. feladat:", end=" ")
db = 0
for i in range(n):
    if matek[i] == 1:
        db += 1
print(db)

#F4
print("4. feladat:", end=" ")
maxi = 0
maxe = (magyar[0] + matek[0] + tori[0]) / 3
for i in range(1, n):
    atlag = (magyar[i] + matek[i] + tori[i]) / 3
    if atlag > maxe:
        maxi = i
        maxe = atlag
print(nevek[maxi])

#F5
print("5. feladat:", end=" ")


# F6
print("6. feladat:", end=" ")


# F7
print("7. feladat:", end=" ")


# F8
print("8. feladat:", end=" ")


# F9
print("9. feladat:", end=" ")


# F10
print("10. feladat:", end=" ")

