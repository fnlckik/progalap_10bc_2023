# Be
alap = float(input("Alap: "))
ertek = float(input("Érték: "))

# Feld
szazalek = ertek / alap * 100

# Ki
# print(round(szazalek, 2), "%", sep="")
# print(f"{round(szazalek, 2)}%")
print(str(round(szazalek, 2)) + "%")