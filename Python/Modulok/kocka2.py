# Dobókockát feldobunk n-szer
# Hány darab 1-est, 2-est, ... 6-ost dobtunk?

from random import randint

n = int(input("Dobások száma: "))
k = int(input("Oldalak száma: "))

# Számláló tömb technika
# count array
# gy[i]: az (i+1)-edik szám gyakoriságát (Hányszor dobtuk?)
# gy = [0, 0, 0, 0, 0, 0]
gy = []
for i in range(k):
    gy.append(0)

for i in range(n):
    r = randint(1, k)
    gy[r-1] += 1

# print(gy)
for i in range(k):
    print(gy[i], end=" ")