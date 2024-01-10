cimek = [
    "Nebula beállna a Nova hadtestbe?",
    "Peter Quill rátámadna a Föld legnagyobb szuperhőseire?",
    "Happy Hogan megmentené a Karácsonyt?",
    "Vasember összetűzésbe keveredne a Nagymesterrel?",
    "Carter Kapitány megküzdene a Hydra-Ölővel?",
    "Kahhori felforgatná a világot?",
    "Hela rátalálna a Tíz Gyűrűre?",
    "a Bosszúállók 1602-ben élnének?",
    "Doctor Strange beavatkozna?"
]

percek = [29, 29, 27, 32, 30, 32, 28, 29, 31]

ertekelesek = [7, 9, 7, 8, 7.5, 8, 9.5, 7, 5]

# F1
n = len(percek)
print("1. Legnépszerűbbek:")
for i in range(n):
    if ertekelesek[i] > 7:
        print("   +", cimek[i])

# F2
maxi = 0
for i in range(1, n):
    if percek[i] > percek[maxi]:
        maxi = i
print("2. Leghosszabb epizód:", cimek[maxi])

# F3
db = 0
for i in range(n):
    if percek[i] < percek[0] and percek[i] < percek[n-1]:
        db += 1
print("3. Rövid közbülső epizódok száma:", db)

# F4
s = 0
for i in range(n):
    s += percek[i]
ora = s // 60
perc = s % 60
print(f"4. A sorozat hossza {ora} óra {perc} perc.")
