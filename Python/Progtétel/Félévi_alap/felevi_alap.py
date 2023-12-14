# Tantárgyak listája
targyak = [
    "Fizika", "Matek",
    "Testnevelés", "Irodalom",
    "Angol", "Történelem",
    "Progalap", "IKT",
    "Digitális kultúra", "ITA",
    "Webprog", "Adatbázis"
]

# Szakmai tantárgy-e?
szakmai = [
    False, False,
    False, False,
    False, False,
    True, True,
    False, True,
    True, True,
]

# Félév végi jegyek
jegyek = [3, 1, 2, 4, 5, 4, 2, 5, 5, 4, 1, 4]

#------------------------------------------------------------------
n = len(jegyek)

# F1
# Összegzés (sorozatszámítás)
osszeg = 0
for i in range(n):
    osszeg += jegyek[i]
atlag = osszeg / n
print("1. Átlag:", round(atlag, 2))

# F2
# Hány darabot teljesített? => megszámolás
db = 0
for i in range(n):
    if jegyek[i] != 1: # jegyek[i] > 1; jegyek[i] >= 2
        db += 1
szazalek = db / n * 100
print(f"2. Teljesített tárgyak aránya: {round(szazalek, 2)}%")

# F3
# Megszámolás
db = 0
for i in range(n):
    if jegyek[i] == 1 and szakmai[i]:
        db += 1
print("3. Bukott szakmai tárgyak száma:", db)

# F4
# Maximum-kiválasztás (index)
maxi = 0
for i in range(1, n):
    if jegyek[i] > jegyek[maxi]:
        maxi = i
print("4. Kedvenc tantárgy:", targyak[maxi])

# F5
# Megszámolás
db = 0
for i in range(n):
    if jegyek[i] > atlag:
        db += 1
print("5. Átlagfeletti tárgyak száma:", db)

# F6


# F7


# F8


# F9


# F10


# F11


# F12
