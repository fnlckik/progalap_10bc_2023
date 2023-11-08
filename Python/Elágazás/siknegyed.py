# Beolvasás
x = float(input("x: "))
y = float(input("y: "))

# Feldolgozás
# Feltesszük, hogy nem tengelyen vagyunk!
if x > 0 and y > 0:
    sn = 1
elif x > 0 and y < 0:
    sn = 4
elif x < 0 and y < 0:
    sn = 3
else:
    sn = 2

# Kiírás
print(f"A megadott pont a(z) {sn}. siknegyedben van!")
