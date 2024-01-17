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
# Eldöntés: Van-e egyes osztályzat?
i = 0
while i < n and not(jegyek[i] == 1):
    i += 1
if i < n:
    print("1. Van amiből bukott!")
else:
    print("1. Átment mindenből!")

# F2: Melyik a leghosszabb nevű tantárgy? (Digitális kultúra)
maxi = 0
for i in range(1, n):
    if len(targyak[i]) > len(targyak[maxi]):
        maxi = i
print("2. Leghosszabb nevű tárgy:", targyak[maxi])

# F3: Van-e olyan tantárgy, amiből ugyanolyan jegyet szerzett, mint irodalomból?
# Feltehető, hogy van "Irodalom" nevű tantárgy!
# Van: (Történelem)
i = 0
while i < n and not(targyak[i] == "Irodalom"):
    i += 1
irodalom = i
j = 0
while j < n and not(jegyek[irodalom] == jegyek[j] and targyak[j] != "Irodalom"):
    j += 1
if j < n:
    print("3.", targyak[j])
else:
    print("3. Semmiből nem kaptunk olyat jegyet, mint irodalomból!")

# F4: Van-e olyan szakmai tárgy, amiből 3-as jegynél rosszabbat kapott?
# Ha igen, akkor add meg az utolsó ilyen tárgy nevét! (Webprog)


# F5: Van-e két egymást követő tantárgy, ami ugyanazzal a betűvel kezdődik?
# Ha igen, add meg a nevüket! (most nincs, de próbáld ki olyan listával is, amikor van)

