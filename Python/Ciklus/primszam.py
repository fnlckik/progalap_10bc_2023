# Írjuk ki, hogy "Prím" vagy "Nem prím"
# prímszám: pontosan 2 osztója van

p = int(input("p: "))

db = 0
for i in range(1, p+1):
    if p % i == 0:
        db += 1

if db == 2:
    print("Prím")
else:
    print("Nem prím")


