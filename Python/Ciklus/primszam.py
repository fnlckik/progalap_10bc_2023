# Beolvasás
# Feltehető, hogy p>=2
p = int(input("p: "))

# Feldolgozás
# 6 => 4
# 24 => 8
# Megszámolás tétele
db = 0
for i in range(1, p+1):
    if p % i == 0:
        db += 1

# Kiírás
# print("Osztók száma:", db)
if db == 2:
    print("Prímszám!")
else:
    print("Nem prímszám!")
