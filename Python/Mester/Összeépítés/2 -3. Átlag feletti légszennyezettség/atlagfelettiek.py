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

# Feld
