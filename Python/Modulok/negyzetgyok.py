x = float(input("x: "))

if x < 0:
    exit()
elif x < 1:
    y = 1 / x
else:
    y = x

also = 1
felso = y
felezo = (also + felso) / 2
while abs(felezo * felezo - y) >= 0.000000001:
    # print(also, felso, felezo)
    if felezo * felezo < y:
        also = felezo
    else:
        felso = felezo
    felezo = (also + felso) / 2

if x < 1:
    felezo = 1 / felezo

print(f"Gyök({x}) = {round(felezo, 30)}")