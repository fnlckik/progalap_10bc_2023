# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))

# Feldolgozás
if a > b and a > c and a > d and a > e:
    legnagyobb = a
elif b > c and b > d and b > e:
    legnagyobb = b
elif c > d and c > e:
    legnagyobb = c
elif d > e:
    legnagyobb = d
else:
    legnagyobb = e

# Kiírás
print("A 4 szám maximuma:", legnagyobb)
