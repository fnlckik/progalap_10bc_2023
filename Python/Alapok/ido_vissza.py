# Beolvasás
mp = int(input("Idő: ")) # 3723

# Feldolgozás
ora = mp // 3600 # 1
maradek = mp % 3600 # 123
perc = maradek // 60 # 2
masodperc = maradek % 60 # 3

# Kiírás
print(f"A nap kezdete óta {ora} óra {perc} perc és {masodperc} másodperc telt el!")
