nev1 = input("1. csapat: ")
nev2 = input("2. csapat: ")
pont1 = int(input("1. pont: "))
pont2 = int(input("2. pont: "))

if pont1 > pont2:
    print(f"{nev1} nyert")
elif pont2 > pont1:
    print(f"{nev2} nyert")
else:
    print("Döntetlen")

