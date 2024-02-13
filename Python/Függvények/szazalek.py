# print("2 / 5 = ", round(2 / 5 * 100), "%", sep="")
# print("2 / 5 = " + str(round(2 / 5 * 100)) + "%")

# Ez függvény?
def kiir(a, b):
    print(f"{a} / {b} = {round(a / b * 100)}%")

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