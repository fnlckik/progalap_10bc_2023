# Beolvasás
csapat1 = input("1. csapat: ")
csapat2 = input("2. csapat: ")
pont1 = int(input("1. pontszám: "))
pont2 = int(input("2. pontszám: "))

# Feldolgozás
if pont1 > pont2:
    kimenet = csapat1 + " nyert"
elif pont2 > pont1:
    kimenet = csapat2 + " nyert"
else:
    kimenet = "Döntetlen"

# Kiírás (gyoztes)
print(kimenet)
