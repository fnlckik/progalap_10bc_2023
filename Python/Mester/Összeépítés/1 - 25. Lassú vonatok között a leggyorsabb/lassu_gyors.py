# Be
n = int(input())
menetidok = []
for i in range(n):
    ido = int(input())
    menetidok.append(ido)
# print(menetidok)

# Feld - feltételes minimum kiválasztás
# Kiválogatás => indexeket kell kiválogatni
lassuak = []
for i in range(n):
    if menetidok[i] > 120:
        lassuak.append(i)
# print(lassuak)

# Minimum-kiválasztás
if lassuak != []:
    mini = lassuak[0] # 1
    for i in range(len(lassuak)): # i = 0, 1, 2, 3
        j = lassuak[i] # j = 1, 2, 4, 5
        if menetidok[j] < menetidok[mini]:
            mini = j
    print(mini+1, menetidok[mini])
else:
    print(-1)
