n = int(input())
nevek, mennyisegek = [], []
adatok = []
for i in range(n):
    sor = input().split() # ["alma", "5"]
    nev = sor[0]
    nevek.append(nev)
    menny = int(sor[1])
    mennyisegek.append(menny)

print("Gyümölcsök:", nevek)
print("Mennyiségek:", mennyisegek)
