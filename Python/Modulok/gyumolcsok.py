from random import randint, randrange, choice

x = ["alma", "barack", "korte", "eper", "banan"]
hossz = len(x)
# Sorsolj ki 20 darab random elemet a listából!
# (A sorsolt elemek ismétlődhetnek.)
# A lista hosszát ne használd ki!

print("MO1:")
for i in range(20):
    # r = randrange(hossz)
    r = randint(0, hossz-1)
    elem = x[r]
    print(i+1, elem)

print("MO2:")
for i in range(20):
    # r = randrange(hossz)
    elem = choice(x)
    print(i+1, elem)