# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

# Feldolgozás
if a >= b and a >= c and a >= d:
    legnagyobb = a
elif b >= a and b >= c and b >= d:
    legnagyobb = b
elif c >= a and c >= b and c >= d:
    legnagyobb = c
else:
    legnagyobb = d

# Kiírás
print("A 4 szám maximuma:", legnagyobb)
