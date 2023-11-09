# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Feldolgozás
D = b*b - 4*a*c
if D < 0:
    mo = 0
elif D == 0:
    mo = 1
else:
    mo = 2

# Kiírás
print(f"Az egyenletnek {mo} darab megoldása van!")
