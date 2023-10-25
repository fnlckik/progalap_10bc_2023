# Beolvasás
n = int(input("Hét napja: "))

# Feldolgozás
if n == 1:
    hetnapja = "Hétfő"
else:
    if n == 2:
        hetnapja = "Kedd"
    else:
        if n == 3:
            hetnapja = "Szerda"
        else:
            if n == 4:
                hetnapja = "Csütörtök"
            else:
                hetnapja = "Péntek"

# Kiírás
print("Ez a nap:", hetnapja)