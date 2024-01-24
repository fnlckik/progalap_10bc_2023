# Be
n = int(input())
menetidok = []
for i in range(n):
    ido = int(input())
    menetidok.append(ido)

# Feld => feltételes minimum kiválasztás
# +vegtelen jelentése: olyan nagy, hogy már biztosan nem fordul elő
vegtelen = 301 
mini = 0
mine = vegtelen
for i in range(n):
    if menetidok[i] < mine and menetidok[i] > 120:
        mini = i
        mine = menetidok[i]

# Ki
# Van adott típusú vonat: 
if mine != vegtelen: # van vonat
    print(mini+1, mine)
else:
    print(-1)

