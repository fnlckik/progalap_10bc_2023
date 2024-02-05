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
munkak = []
for i in range(n):
    if percek[i] < 10:
        munkak.append(nevek[i])
print(len(munkak), *munkak)
# print(len(munkak), end=" ")
# for i in range(len(munkak)):
#     print(munkak[i], end=" ")
# print()

# F3 - Keresés
print("3. feladat: ", end="")
# Több mint 2 óra: több mint 120 perc
i = 0
while i < n and not(percek[i] * gyakorisagok[i] > 120):
    i += 1
if i < n:
    print(nevek[i])
else:
    print(-1)

# F4 - Feltételes maximum
print("4. feladat: ", end="")
# MO1 - Tudunk maximális értékre korlátokat (alsó, felső)
maxi = -1
maxe = -1
for i in range(n):
    if percek[i] <= 60 and percek[i] > maxe:
        maxi = i
        maxe = percek[i]
if maxe != -1:
    print(nevek[maxi])
else:
    print("Nincs ilyen!")

# MO2 - Keresés + Maximum
# i = 0
# while i < n and not(percek[i] <= 60):
#     i += 1
# if i < n:
#     maxi = i
#     for i in range(i+1, n):
#         if percek[i] <= 60 and percek[i] > percek[maxi]:
#             maxi = i
#     print(nevek[maxi])
# else:
#     print("Nincs ilyen!")

# MO3 - Kiválogatás + Maximum
# rovidek = []
# for i in range(n):
#     if percek[i] <= 60:
#         rovidek.append(i)
# if rovidek == []:
#     print("Nincs ilyen!")
# else:
#     maxi = rovidek[0]
#     for i in range(len(rovidek)):
#         if percek[rovidek[i]] > percek[maxi]:
#             maxi = rovidek[i]
#     print(nevek[maxi])

# F5
print("5. feladat: ")
ido = 0
for i in range(n):
    ido += percek[i] * gyakorisagok[i]
ora = ido // 60
perc = ido % 60
print(f"a) Heti munka (ora, perc): {ora} {perc}")

het = 7*24*60
arany = ido / het * 100
print(f"b) Heti arány (%): {round(arany, 2)}")

# F6 - Bónusz - Összegzés + Keresés
print("6. feladat: ", end="")
s = 0
for i in range(n):
    s += len(nevek[i])
atlag = s / n
# print(atlag)

i = n-2
while i > 0 and not(gyakorisagok[i] == 1 and percek[i] > percek[i+1] and percek[i] > percek[i-1] and len(nevek[i]) > atlag):
    i -= 1
if i > 0:
    print(nevek[i])