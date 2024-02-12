from random import randint

n = int(input("n: "))

# db1 = 0
# db2 = 0
# db3 = 0
# db4 = 0
# db5 = 0
# db6 = 0
db1, db2, db3, db4, db5, db6 = 0, 0, 0, 0, 0, 0
for i in range(n):
    r = randint(1, 6)
    print(r, end=" ")
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
    else:
        db6 += 1

print()
print("-"*25)
# Hány darab 1, 2, 3... számot dobtunk?
print(db1, db2, db3, db4, db5, db6)