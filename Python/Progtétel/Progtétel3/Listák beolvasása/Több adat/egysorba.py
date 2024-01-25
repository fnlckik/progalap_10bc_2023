n = int(input())
nevek = []
darabok = []

for i in range(n):
    sor = input().split() # ["alma", 5]
    nev = sor[0]
    db = int(sor[1])
    nevek.append(nev)
    darabok.append(db)

print("Gyümölcsök:", nevek)
print("Mennyiségek:", darabok)
