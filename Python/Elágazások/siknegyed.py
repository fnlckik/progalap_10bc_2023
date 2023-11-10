# Beolvasás
x = float(input("x: "))
y = float(input("y: "))

# Feldolgozás
if x > 0 and y > 0:
    sn = 1
elif x < 0 and y > 0:
    sn = 2
elif x < 0 and y < 0:
    sn = 3
else:
    sn = 4

# Kiírás
print(f"A(z) {sn} síknegyedben van!")
