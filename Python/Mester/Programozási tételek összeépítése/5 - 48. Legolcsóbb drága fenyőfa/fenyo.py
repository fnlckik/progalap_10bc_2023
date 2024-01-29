# Be
be = input().split() # ["6", "5000"]
n = int(be[0])
k = int(be[1])
arak = []
for i in range(n):
    ar = int(input())
    arak.append(ar)
# print(arak)

# Feld - feltételes minimum kiválasztás
mini = -1
mine = 10001
for i in range(n):
    if arak[i] > k and arak[i] < mine:
        mini = i
        mine = arak[i]

# Ki
if mine != 10001:
    print(mini+1, mine)
else:
    print(-1)
