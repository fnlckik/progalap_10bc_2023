# print("2 / 5 = ", round(2 / 5 * 100), "%", sep="")
# print("2 / 5 = " + str(round(2 / 5 * 100)) + "%")

# Ez függvény? => "Nem" => Function
# "Gond": Nem ad vissza semmit(?)

# Ez egy eljárás! => Procedure
# Eljárás: olyan alprogram, ami elvégez egy feladatot
# de "nincs" visszatérési értéke
def kiir(a, b):
    print(f"{a} / {b} = {round(a / b * 100)}%")

kiir(2, 5)
kiir(2, 3)
kiir(5, 7)
kiir(5, 37)
kiir(50, 307)

# print(f"2 / 5 = {round(2 / 5 * 100)}%")
# print(f"2 / 3 = {round(2 / 3 * 100)}%")
# print(f"5 / 7 = {round(5 / 7 * 100)}%")
# print(f"5 / 37 = {round(5 / 37 * 100)}%")
# print(f"50 / 307 = {round(50 / 307 * 100)}%")

# "Tarsd szárazon a kódod!" DRY
# DRY: Don't repeat yourself!