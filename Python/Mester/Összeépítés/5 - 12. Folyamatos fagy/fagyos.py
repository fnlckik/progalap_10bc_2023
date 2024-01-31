# Be
elsosor = input().split()
n = int(elsosor[0])
k = int(elsosor[1])
minek, maxok = [], []
for i in range(n):
    sor = input().split()
    minek.append(int(sor[0]))
    maxok.append(int(sor[1]))
# print(maxok)

# Feld - Másolás + Keresés
# x[i]: i-edik nap legfeljebb hányadik napja lehet az intervallumnak
x = []
if maxok[0] < 0:
    x.append(1)
else:
    x.append(0)
for i in range(1, n):
    if maxok[i] >= 0:
        x.append(0)
    else:
        elozo = x[i-1]
        x.append(elozo + 1)
    # elif maxok[i] < 0 and maxok[i-1] < 0:
    #     elozo = x[i-1]
    #     x.append(elozo + 1)
    # else:
    #     x.append(1)
# print(x)

# Ki
i = 0
while i < n and not(x[i] == k):
    i += 1
if i < n:
    eleje = i+1 - (k-1)
    vege = i+1
    print(eleje, vege)
else:
    print(-1)
    