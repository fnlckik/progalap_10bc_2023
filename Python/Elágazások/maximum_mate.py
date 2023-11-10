# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Feldolgozás + Kiírás
if a >= b and a >= c:
    print(a, end="")
elif b >= a and b >= c:
    print(b, end="")
else:
    print(c, end="")

print(" a legnagyobb")