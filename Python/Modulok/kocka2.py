from random import randint

n = int(input("n: "))
oldalszam = int(input("oldalszam: "))

# gyakorisagok[i]: az (i+1)-ből hányat dobtunk?
# gyakorisagok = [0, 0, 0, 0, 0, 0]
# gyakorisagok = [0] * 6

# Másolás tétel: legyen egy 6 elemű listánk 0-kal teli
gyakorisagok = []
for i in range(oldalszam):
    gyakorisagok.append(0)

# Számláló tömb technika
# Count array technique
for i in range(n):
    r = randint(1, oldalszam) #5
    gyakorisagok[r-1] += 1 #4
    print(gyakorisagok)
    # print(r, end=" ")


print()
print("-"*25)
# Hány darab 1, 2, 3... számot dobtunk?
# print(*gyakorisagok)

for i in range(oldalszam):
    print(gyakorisagok[i], end=" ")
    