# Pozitív egész osztókat írjuk ki!
# 12 => 1 2 3 4 6 12

# Kiválogatás tétel
n = int(input("n: "))
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
