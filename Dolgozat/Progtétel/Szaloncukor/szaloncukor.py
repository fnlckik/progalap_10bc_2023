# Szaloncukor típusok
tipusok = ["kókuszos", "gumicukor", "epres", "zselés", "marcipános", "banános", "oreos", "alkoholos"]

# Eladott mennyiségek egy hét alatt (kg-ban)
mennyisegek = [25, 30, 12, 48, 15, 18, 31, 16]

# Egységár (1kg szaloncukor ára forintban)
arak = [2200, 3800, 2800, 3500, 3500, 3000, 4200, 5400]

# F1
n = len(arak)
print("A kínálat:")
for i in range(n):
    print(f"  {i+1}. {tipusok[i]} - {arak[i]} Ft/kg")

# F2
maxi = 0
for i in range(1, n):
    if mennyisegek[i] > mennyisegek[maxi]:
        maxi = i
print("A legnépszerűbb típus:", tipusok[maxi])

# F3
db = 0
for i in range(n):
    if 2000 <= arak[i] and arak[i] <= 3000:
        db += 1
print("A 2000 és 3000 Ft közöttiek száma:", db)

# F4
s = 0
for i in range(n):
    aktualis = mennyisegek[i] * arak[i]
    s += aktualis
print("A heti bevétel:", s, "Ft")

