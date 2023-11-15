# Bemenet: a (valós), k (nemneg. egész)
# Kimenet: a-nak a k-adik hatványa

# a = 2; b = 3
# hatvany = 8

# a = 3; b = 4
# hatvany = 81

# a = 2; b = 5
# hatvany = 32 (2*2*2*2*2)

# Beolvasás
a = float(input("a: "))
k = int(input("k: "))

# Feldolgozás
hatvany = 1
for i in range(k):
    hatvany *= a
    # hatvany = hatvany*a

# Kiírás
print("Hatvány:", hatvany)
