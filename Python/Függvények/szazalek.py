# print("2 / 5 = ", round(2 / 5 * 100), "%", sep="")
# print("2 / 5 = " + str(round(2 / 5 * 100)) + "%")

# Ez függvény? => "Nem"
# "Nincs return" (visszatérési érték)
# Ez eljárás!
# Function => return
# Procedure => nincs return
def kiir(a, b):
    szazalek = round(a / b * 100)
    print(f"{a} / {b} = {szazalek}%")

kiir(2, 5)
kiir(2, 3)
kiir(7, 13)
kiir(13, 42)
kiir(82, 13)  
# print(f"2 / 5 = {round(2 / 5 * 100)}%")
# print(f"2 / 3 = {round(2 / 3 * 100)}%")
# print(f"7 / 13 = {round(7 / 13 * 100)}%")
# print(f"13 / 42 = {round(13 / 42 * 100)}%")
# print(f"82 / 13 = {round(82 / 13 * 100)}%")

# "Tarts szárazon a kódod!" DRY
# DRY: Don't repeat yourself!

# Mellékhatás: 
# egy fv csinál valami mást is a számolás mellet
# Pl.: értéket módosít, kiír valamit...

# Fv-ek legyenek mellékhatás mentesek!