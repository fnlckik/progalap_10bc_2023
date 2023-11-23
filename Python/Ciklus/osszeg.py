# n => 1 + 2 + 3 + ... + n = ???
# 5 => 1 + 2 + 3 + 4 + 5 = 15
# 8 => 1 + 2 + ... + 8 = 36

# Beolvasás
n = int(input("n: "))

# Feldolgozás
osszeg = 0
for i in range(1, n+1):
    osszeg = osszeg + i

# Kiírás
print("Összeg:", osszeg)