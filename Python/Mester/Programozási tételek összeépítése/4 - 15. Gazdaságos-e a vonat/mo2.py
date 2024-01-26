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

# Feld
letszam = 0
bevetel = 0
for i in range(n):
    letszam = letszam + felszallok[i] - leszallok[i]
    bevetel += letszam * ar

# Ki
if bevetel > koltseg * (n-1):
    print(1)
else:
    print(0)
