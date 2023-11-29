# Beolvasás
a = int(input("a: "))
b = int(input("b: "))
kecske = int(input("Kezdőpont: "))

# Feldolgozás
while a <= kecske and kecske <= b:
    if kecske % 2 == 0:
        kecske += 5
    elif kecske % 3 == 0:
        kecske -= 7
    else:
        kecske += 1

# Kiírás
print(f"A kecske a {kecske} számnál hagyta el a telket!")