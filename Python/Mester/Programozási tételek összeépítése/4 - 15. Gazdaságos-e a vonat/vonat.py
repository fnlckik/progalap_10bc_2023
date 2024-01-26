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

# Feld - Másolás + Összegzés
bevetelek = []
letszam = 0
for i in range(n-1):
    letszam = letszam + felszallok[i] - leszallok[i]
    bevetel = ar * letszam
    bevetelek.append(bevetel) 
# print(bevetelek)

osszbevetel = 0
for i in range(len(bevetelek)):
    osszbevetel += bevetelek[i]

osszkoltseg = (n-1) * koltseg

# Ki
if osszbevetel > osszkoltseg:
    print(1)
else:
    print(0)
