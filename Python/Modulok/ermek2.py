from random import randint

# Dobjunk fel egy érmét 100-szor!
# Írjuk ki, hogy F vagy I oldalt kaptunk!

n = int(input("Dobások száma: "))

# F = 1, I = 2
fejDb = 0
irasDb = 0
for i in range(n):
    r = randint(1, 2)
    if r == 1:
        fejDb += 1
    else:
        irasDb += 1
print()

# Fejek gyakorisága: hány darab van?
print("Fejek száma:", fejDb)
print("Írások száma:", irasDb)

# Fejek relatív gyakorisága: 
# gyakoriság az összeshez viszonyítva
# gyakorisag / dobasszam
print("Fejek rel. gyak.:", fejDb / n)
print("Írások rel. gyak.:", irasDb / n)
