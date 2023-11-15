# Beolvasás
a = float(input("a: "))
k = int(input("k: "))

# Feldolgozás
hatvany = 1
i = 1
while i <= k:
    hatvany *= a
    i += 1

# Kiírás
print("Hatvány:", hatvany)
