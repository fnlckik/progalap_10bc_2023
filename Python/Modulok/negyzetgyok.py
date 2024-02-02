# Felezési eljárás
# Lásd később: bináris keresés

# Mennyi gyök(2)? => 1.414
x = float(input("x: "))

if x >= 1:
    y = x
else:
    y = 1 / x

also = 0
felso = y
felezo = (also + felso) / 2

while abs(felezo * felezo - y) >= 0.000001:
    # print(also, felso, felezo)
    if felezo * felezo < y:
        also = felezo
    else:
        felso = felezo
    felezo = (also + felso) / 2

if x < 1:
    felezo = 1 / felezo

print(f"Gyök({x}) = {round(felezo, 3)}")