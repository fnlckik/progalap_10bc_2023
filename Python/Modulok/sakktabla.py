n = int(input("Sorok száma: "))
m = int(input("Oszlopok száma: "))

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("0", end=" ")
    print()
