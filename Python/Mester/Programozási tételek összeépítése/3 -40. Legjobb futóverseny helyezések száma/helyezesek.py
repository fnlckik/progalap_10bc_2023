# Be
n = int(input())
helyezesek, percek, mpercek = [], [], []
for i in range(n):
    sor = input().split() # ["4", "3", "12"]
    hely = int(sor[0])
    helyezesek.append(hely)
    perc = int(sor[1])
    percek.append(perc)
    mperc = int(sor[2])
    mpercek.append(mperc)
# print(helyezesek)
# print(percek)
# print(mpercek)

# Feld - Min + Megszámolás
mine = helyezesek[0]
for i in range(1, n):
    if helyezesek[i] < mine:
        mine = helyezesek[i]

db = 0
for i in range(n):
    if helyezesek[i] == mine:
        db += 1

# Ki
print(mine, db)
