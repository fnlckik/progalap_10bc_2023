tipusok = [
    "Trabant", "Skoda", "Volkswagen",
    "Dacia", "Polski Fiat", "Moszkvics",
    "Wartburg", "Fiat", "Lada",
    "Renault"
]

mennyisegek = [
    264900, 184400, 5100,
    40600, 65700, 43300,
    183900, 15500, 352100,
    4400
]

# F1
n = len(mennyisegek)
i = 0
while i < n and not(tipusok[i] == "Volkswagen"):
    i += 1
if i < n:
    print("1. Volkswagen eladott mennyiség:", mennyisegek[i])
else:
    print("1. Nincs Volkswagen a listában!")

# F2
mini = 0
for i in range(1, n):
    if len(tipusok[i]) < len(tipusok[mini]):
        mini = i
print("2. Legrövidebb nevű autó:", tipusok[mini])

# F3
# Eldöntés: Van-e olyan, hogy nagyobbat kisebb követ?
i = 0
while i < n-1 and not(mennyisegek[i-1] < mennyisegek[i]):
    i += 1
if i < n-1:
    print("3. Nem monoton növekedők")
else:
    print("3. Monoton növekedők")

# F4
i = n-1
while i >= 0 and not(10000 <= mennyisegek[i] and mennyisegek[i] <= 50000):
    i -= 1
if i >= 0:
    print("4. Utolsó autó sorszáma, amelyből 10 és 50 ezer közöttit adtak el:", i+1)

# F5
s = 1
i = 1
while i <= 50 and not(s % 10000 == 0):
    i += 1
    s += i**5
if i <= 50:
    print(f"A sorozat {i}. tagja osztható 10000-rel: {s}")
