# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Feldolgozás
legnagyobb = a
if b > legnagyobb:
    legnagyobb = b
if c > legnagyobb:
    legnagyobb = c

# Kiírás
print("A 3 szám maximuma:", legnagyobb)
