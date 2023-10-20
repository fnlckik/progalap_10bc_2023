# Be
ora = int(input("Óra: "))
perc = int(input("Perc: "))
mperc = int(input("Másodperc: "))

# Feld
mpercben = ora * 3600 + perc * 60 + mperc

# Ki
print(f"A nap kezdete óra {mpercben} másodperc telt el.")