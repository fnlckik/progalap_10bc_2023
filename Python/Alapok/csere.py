# Beolvasás
a = int(input("1. sorszám: "))
b = int(input("2. sorszám: "))
print("Eredetileg:", a, b)

# a: 3
# b: 7
# Feldolgozás
seged = a
a = b
b = seged
# a, b = b, a

# Kiírás
print("Fordítva:", a, b)
