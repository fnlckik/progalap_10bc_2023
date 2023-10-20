# Beolvasás
hosszusag = int(input("Telek hossza: ")) # "2" => 2
szelesseg = int(input("Telek szélessége: ")) # "3" => 3
kapu = int(input("Kapu szélessége: "))

# Feldolgozás
kerulet = 2 * (hosszusag + szelesseg) # 2 * (2 + 3) == 10
kerites = kerulet - kapu

# Kiírás
print(f"A telek kerítése: {kerites}m")
print("A telek kerítése: " + str(kerites) + "m")
print("A telek kerítése: ", kerites, "m", sep="")