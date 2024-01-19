# Beolvasás
n = int(input()) # vonatok szama
k = int(input()) # küszöbérték
menetidok = []
for i in range(n):
    ido = int(input())
    menetidok.append(ido)

# Feldolgozás - kiválogatás
megoldasok = []
for i in range(n):
    if menetidok[i] < k:
        megoldasok.append(i+1)

# Kiírás - Kiírjuk a megoldások elemeit!
print(len(megoldasok), end=" ")
for i in range(len(megoldasok)):
    print(megoldasok[i], end=" ")
