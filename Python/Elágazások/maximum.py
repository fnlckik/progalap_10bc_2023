# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Feldolgozás
# a==b and a>c
# a:2 b:2 c:1
if a >= b and a >= c:
    legnagyobb = a
elif b >= a and b >= c:
    legnagyobb = b
else:
    legnagyobb = c

# Kiírás
print("A 3 szám maximuma:", legnagyobb)
