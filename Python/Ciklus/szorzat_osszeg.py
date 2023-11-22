# 1
# 1*2 => 2

# 2
# 1*2 + 2*3 => 8

# 3
# 1*2 + 2*3 + 3*4 => 2 + 6 + 12 => 20

n = int(input("n: "))

osszeg = 0
for i in range(1, n+1):
    aktualis = i*(i+1)
    osszeg += aktualis

    print(f"{i}*{i+1}", end="")
    if i == n:
        print(" = ", end="")
    else:
        print(" + ", end="")

print(osszeg)