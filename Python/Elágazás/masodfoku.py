# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Feldolgozás
# D = b*b - 4*a*c
D = b**2 - 4*a*c
if D < 0:
    megoldasok_szama = 0
elif D == 0:
    megoldasok_szama = 1
else:
    megoldasok_szama = 2

# Kiírás
print("Megoldások száma:", megoldasok_szama)
