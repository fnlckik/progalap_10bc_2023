# Beolvasás
a = float(input("a: "))
k = int(input("k: "))

# Feldolgozás
hatvany = a
for i in range(k-1):
    hatvany *= a

# Kiírás
print("Hatvány:", hatvany)
