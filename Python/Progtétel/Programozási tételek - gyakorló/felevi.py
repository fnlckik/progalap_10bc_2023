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
i = 0
while i < n and not(matek[i] > magyar[i]):
    i += 1
if i < n:
    print(nevek[i])
else:
    print("Nincs")

# F6
print("6. feladat:", end=" ")
vegzodesek = []
for i in range(n):
    nev = nevek[i] # Oliver
    hossz = len(nev) # 6
    if nev[hossz-1] == "a": # 5
        vegzodesek.append(nevek[i])
print(len(vegzodesek), end=" ")
# print(*vegzodesek)
for i in range(len(vegzodesek)):
    print(vegzodesek[i], end=" ")
print()

# F7
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
mine = 6 # +vegtelen
for i in range(n):
    if magyar[i] == 5 and matek[i] <= mine:
        mini = i
        mine = matek[i]
if mine != 6:
    print(nevek[mini])
else:
    print(-1)

# F9
print("9. feladat:", end=" ")
db = 0
for i in range(n):
    if magyar[i] == 1 or matek[i] == 1 or tori[i] == 1:
        db += 1
arany = db / n * 100
print(f"{round(arany, 2)}%")

# F10
print("10. feladat:", end=" ")
cserelnenek = []
for i in range(1, n-1):
    if matek[i] < matek[i-1] and matek[i] < matek[i+1]:
        cserelnenek.append(i+1)
# print(*cserelnenek)
for i in range(len(cserelnenek)):
    print(cserelnenek[i], end=" ")
