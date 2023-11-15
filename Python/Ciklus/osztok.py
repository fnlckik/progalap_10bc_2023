# Kapunk egy egész számot!
# Írjuk ki a pozitív egész osztóit!

# Minta:
# n: 6
# 1 2 3 6

# Minta:
# n: 24
# 1 2 3 4 6 8 12 24

# Beolvasás
n = int(input("n: "))

# Feldolgozás + Kiírás
# Kiválogatás tétele
print("A szám osztói:")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")

