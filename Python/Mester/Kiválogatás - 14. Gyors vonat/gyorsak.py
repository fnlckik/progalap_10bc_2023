# Beolvasás - lista beolvasás
n = int(input())
k = int(input())
menetidok = []
for i in range(n):
    m = int(input())
    menetidok.append(m)

# Feldolgozás - kiválogatás
gyorsak = []
for i in range(n):
    if menetidok[i] < k:
        gyorsak.append(i+1)

# Kiírás
print(len(gyorsak), end=" ")
for i in range(len(gyorsak)):
    print(gyorsak[i], end=" ")
