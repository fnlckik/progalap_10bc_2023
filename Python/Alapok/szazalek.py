# Be
alap = int(input("Alap: "))
ertek = int(input("Érték: "))

# Feld
szazalek = ertek / alap * 100

# Ki
print(round(szazalek, 2), "%", sep="")
print(str(round(szazalek, 2)) + "%")
print(f"{round(szazalek, 2)}%")
