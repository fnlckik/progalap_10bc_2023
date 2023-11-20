# Írjuk ki, hogy "Prím" vagy "Nem prím"
# prímszám: pontosan 2 osztója van

p = int(input("p: "))

# Keresek 1-nél nagyobb p-nél kisebb osztót (kezdetben nincs)
oszto = 0
i = 2
while i < p and oszto == 0: # csak addig megyek amig nincs oszto
    if p % i == 0:
        oszto = i
    i += 1

# Ha nem találtam 1-nél nagyobb p-nél kisebb osztót akkor prím
if oszto == 0:
    print("Prím")
else:
    print("Nem prím")


