# Beolvasás
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# Feldolgozás
if a + b > c and b + c > a and c + a > b:
    kimenet = "Szerkeszthető!"
else:
    kimenet = "Nem szerkeszthető!"

# Kiírás
print(kimenet)
