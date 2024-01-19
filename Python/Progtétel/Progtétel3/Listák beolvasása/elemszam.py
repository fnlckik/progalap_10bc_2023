# szamok = [2, 7, 8, -1, 7, 12]

# Olvass be N egész számot
# egy listába!
# Először: 5 db

n = int(input())

szamok = []
for i in range(n):
    szam = int(input())
    szamok.append(szam)

# Mit csinálunk a listával?
print("Beolvasott lista:", szamok)

s = 0
for i in range(n):
    s += szamok[i]
print("Elemek összege:", s)

parosak = []
for i in range(n):
    if szamok[i] % 2 == 0:
        parosak.append(szamok[i])
print("Párosak:", parosak)
