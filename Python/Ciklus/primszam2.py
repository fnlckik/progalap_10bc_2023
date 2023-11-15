# Beolvasás
# Feltehető, hogy p>=2
p = int(input("p: "))

# Feldolgozás
# Eldöntés tétele
db = 0
i = 1
while i <= p and db <= 2:
    if p % i == 0:
        db += 1
    i += 1

# Kiírás
if db == 2:
    print("Prímszám!")
else:
    print("Nem prímszám!")
