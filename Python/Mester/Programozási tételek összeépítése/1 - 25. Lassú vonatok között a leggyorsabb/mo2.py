# Be
n = int(input())
menetidok = []
for i in range(n):
    x = int(input())
    menetidok.append(x)

# Feltételes minimum
mini = 0
mine = 301 # biztosan túl nagy érték (+ végtelen)
for i in range(n):
    if menetidok[i] > 120 and menetidok[i] < mine:
        mini = i
        mine = menetidok[i]

if mine == 301:
    print(-1)
else:
    print(mini+1, mine)
