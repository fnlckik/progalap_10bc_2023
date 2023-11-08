# Beolvasás
suly = float(input("Csomag súlya (kg): "))
tav = int(input("Csomag távolsága (km): "))

# Feldolgozás
if suly < 5 and tav < 500:
    dij = 20
elif suly < 5 and tav >= 500:
    dij = 35
elif suly >= 5 and tav < 500:
    dij = 30
else:
    dij = 50

# Kiírás
print(f"A szállítás díja {dij}$.")
