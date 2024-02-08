n = int(input())
nevek, percek, gyakorisagok = [], [], []
for i in range(n):
    sor = input().split()
    nev = sor[0]
    nevek.append(nev)
    perc = int(sor[1])
    percek.append(perc)
    gyakorisag = int(sor[2])
    gyakorisagok.append(gyakorisag)
# print(gyakorisagok)

# F2 - Kiválogatás
print("2. feladat: ", end="")
rovidek = []
db = 0
for i in range(n):
    if percek[i] < 10:
        db += 1
        rovidek.append(nevek[i])
print(db, end=" ")
for i in range(db):
    print(rovidek[i], end=" ")
print()
# print(db, *rovidek)

# F3 - Keresés
print("3. feladat: ", end="")
i = 0
while i < n and not(percek[i]*gyakorisagok[i] > 120):
    i += 1
if i < n:
    print(nevek[i])
else:
    print(-1)

# F4
print("4. feladat: ", end="")
# MO1
maxi = -1
maxe = -1 # -végtelen
for i in range(n):
    if percek[i] <= 60 and percek[i] > maxe:
        maxi = i
        maxe = percek[i]
if maxe != -1:
    print(nevek[maxi])
else:
    print("Nincs ilyen!")

# F5
print("5. feladat: ")
ido = 0
for i in range(n):
    ido += percek[i] * gyakorisagok[i]
ora = ido // 60
perc = ido % 60
print(f"a) Heti munka (ora, perc): {ora} {perc}")
arany = ido / (7*24*60) * 100
print(f"b) Heti arány (%): {round(arany, 20)}")

# F6 - Bónusz
print("6. feladat: ", end="")
atlag = 0
for i in range(n):
    atlag += len(nevek[i])
atlag = atlag / n

i = n-2
while i > 0 and not(gyakorisagok[i] == 1 and percek[i] > percek[i-1] and percek[i] > percek[i+1] and len(nevek[i]) > atlag):
    i -= 1
if i > 0:
    print(nevek[i])

