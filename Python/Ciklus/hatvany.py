# Beolvasás
alap = float(input("a: "))
n = int(input("n: "))

# Feldolgozás
# Sorozatszámítás
hatvany = 1
for i in range(n):
    hatvany = hatvany * alap

# Kiírás
# a^k, a^n
print("Hatvány:", hatvany)
