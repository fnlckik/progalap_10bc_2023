# Írjuk ki, hogy "Prím" vagy "Nem prím"
# prímszám: pontosan 2 osztója van

p = int(input("p: "))

oszto = 0
i = 2
while i < p and oszto == 0:
    if p % i == 0:
        oszto = i
    i += 1

if oszto == 0:
    print("Prím")
else:
    print("Nem prím")


