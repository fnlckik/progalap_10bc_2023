# Dobókockát feldobunk n-szer
# Hány darab 1-est, 2-est, ... 6-ost dobtunk?

from random import randint

n = int(input("Dobások száma: "))

# db1 = 0
# db2 = 0
# db3 = 0
# db4 = 0
# db5 = 0
# db6 = 0
db1, db2, db3, db4, db5, db6 = 0, 0, 0, 0, 0, 0
for i in range(n):
    r = randint(1, 6)
    # print(r, end=" ")
    if r == 1:
        db1 += 1
    elif r == 2:
        db2 += 1
    elif r == 3:
        db3 += 1
    elif r == 4:
        db4 += 1
    elif r == 5:
        db5 += 1
    elif r == 6:
        db6 += 1
print()

# Ki
print(db1, db2, db3, db4, db5, db6)