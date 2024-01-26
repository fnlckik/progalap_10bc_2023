# Be
n = int(input())
reggeliek, estiek = [], []
for i in range(n):
    sor = input().split() # ["100", "120"]
    reggeli = int(sor[0])
    reggeliek.append(reggeli)
    esti = int(sor[1])
    estiek.append(esti)

# print(reggeliek)
# print(estiek)

# Feld - Összegzés + Kiválogatás
s = 0
for i in range(n):
    s += estiek[i]
atlag = s / n

nagyok = []
for i in range(n):
    if estiek[i] > atlag:
        nagyok.append(i)

# Ki
print(len(nagyok), end=" ")
for i in range(len(nagyok)):
    print(nagyok[i]+1, end=" ")
