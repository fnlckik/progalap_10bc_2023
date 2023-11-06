# Beolvasás
szelesseg = int(input("Szélesség: "))
hosszusag = int(input("Hosszúság: "))
p = float(input("Szélesség növelése: "))
q = float(input("Hosszúság növelése: "))

# Feldolgozás
'''
terulet = szelesseg * hosszusag
terulet_uj = szelesseg * (1 + p/100) * hosszusag * (1 + q/100)
hanyados = round(terulet_uj / terulet, 2)
'''
hanyados = round((1 + p/100) * (1 + q/100), 2)

# Kiírás
print(f"Nagyjából {hanyados}x akkora lesz a telek!")
print("Nagyjából ", hanyados, "x akkora lesz a telek!", sep="")
print("Nagyjából " + str(hanyados) + "x akkora lesz a telek!")
