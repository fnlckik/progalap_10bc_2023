ev = int(input("Év: "))

if ev <= 2000:
    print("Hiba! Nem 2000 feletti év!")
    exit()

if ev % 4 == 0:
    print("Szőkőév!")
else:
    print("Nem szökőév!")
