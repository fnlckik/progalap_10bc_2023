# Beolvasás
n = int(input("n: "))

# Feldolgozás
osszeg = 0
for i in range(1, n+1):
    aktualis = 1/i
    if i % 2 == 0:
        osszeg -= aktualis
    else:
        osszeg += aktualis

# Kiírás
print(f"A kapott összeg: {round(osszeg, 5)}")
