# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Feldolgozás
if a > b and a > c:
    legnagyobb = a
elif b > c: # a<=b or a<=c
    legnagyobb = b
else:
    legnagyobb = c

# Kiírás
print("A 3 szám maximuma:", legnagyobb)
