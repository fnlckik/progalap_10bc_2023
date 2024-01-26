# Be
n = int(input())
nappaliak, estiek = [], []
for i in range(n):
    sor = input().split() # "100 200" => ["100", "200"]
    nappali = int(sor[0]) # 100
    esti = int(sor[1]) # 200
    nappaliak.append(nappali)
    estiek.append(esti)

# print(nappaliak)
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
