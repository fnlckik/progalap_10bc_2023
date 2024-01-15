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

# F1: Igaz-e, hogy minden tárgyból átment? (nem igaz)
# Eldönt: Van-e tárgy, amiből megbukott?
i = 0
while i < n and not(jegyek[i] == 1):
    i += 1
if i < n:
    print("1. Nem igaz, hogy minden tárgyból átment!")
else:
    print("1. Minden tárgyból átment!")

# F2: Melyik a leghosszabb nevű tantárgy? (Digitális kultúra)
maxi = 0
for i in range(1, n):
    if len(targyak[i]) > len(targyak[maxi]):
        maxi = i
print("2. A leghosszabb nevű tárgy:", targyak[maxi])

# F3: Van-e olyan tantárgy, amiből ugyanolyan jegyet szerzett, mint irodalomból?
# Feltehető, hogy van "Irodalom" nevű tantárgy!
# Van: (Történelem)
# 1. lépés: válasszuk ki az irodalom indexét!
i = 0
while not(targyak[i] == "Irodalom"):
    i += 1
irodalom = i
# 2. lépés: keressünk egy másik tárgyat, amiből szintén ezt a jegyet kapta
i = 0
while i < n and not(jegyek[i] == jegyek[irodalom] and i != irodalom):
    i += 1
if i < n:
    print("3. Ugyanolyan jegy, mint irodalomból:", targyak[i])

# F4: Van-e olyan szakmai tárgy, amiből 3-as jegynél rosszabbat kapott?
# Ha igen, akkor add meg az utolsó ilyen tárgy nevét! (Webprog)


# F5: Van-e két egymást követő tantárgy, ami ugyanazzal a betűvel kezdődik?
# Ha igen, add meg a nevüket! (most nincs, de próbáld ki olyan listával is, amikor van)

