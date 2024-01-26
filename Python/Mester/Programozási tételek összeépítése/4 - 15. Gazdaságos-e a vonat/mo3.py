# Be
n = int(input())
be = input().split() # ["100", "1000"]
ar = int(be[0])
koltseg = int(be[1])

leszallok, felszallok = [], []
for i in range(n):
    sor = input().split() # ["0", "15"]
    le = int(sor[0])
    leszallok.append(le)
    fel = int(sor[1])
    felszallok.append(fel)

# print(leszallok)
# print(felszallok)

# Feld - Keresés
letszam = 0
osszkoltseg = koltseg * (n-1)
osszbevetel = 0
i = 0
while i < n and not(osszbevetel > osszkoltseg):
    letszam = letszam + felszallok[i] - leszallok[i]
    osszbevetel += letszam * ar
    i += 1

# Ki
if i < n:
    print(1)
else:
    print(0)