# Be
mperc = int(input("Másodperc: ")) # 10862

# Feld
ora = mperc // 3600 # 3
maradek = mperc % 3600 # 62
perc = maradek // 60 # 1
masodperc = maradek % 60 # 2

# Ki
# print(f"A nap kezdete óta {ora} óra, {perc} perc, és {masodperc} másodperc telt el!")
print("A nap kezdete óta", ora, "óra,", perc, "perc, és", masodperc, "másodperc telt el.")
# print("A nap kezdete óta " + str(ora) + " óra, " + str(perc) + " perc, és " + str(masodperc) + " masodperc telt el.")