from random import randint, randrange

x = ["alma", "barack", "korte", "eper", "banan"]
hossz = len(x)
# Sorsolj ki 20 darab random elemet a listából!
# (A sorsolt elemek ismétlődhetnek.)
# A lista hosszát ne használd ki!

for i in range(20):
    # r = randint(0, hossz-1)
    r = randrange(hossz)
    print(i+1, x[r])
