# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

# Feldolgozás
legnagyobb = a
if b > legnagyobb:
    legnagyobb = b
if c > legnagyobb:
    legnagyobb = c
if d > legnagyobb:
    legnagyobb = d

# Kiírás
print("A legnagyobb:", legnagyobb)