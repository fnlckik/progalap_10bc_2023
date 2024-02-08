from random import randrange, randint

# 5 és 8 közötti számokat!
# Vigyázat! Hasonló a range()-hez
# range(a, b) => [a, b)
print("5 és 8 közötti számok:")
for i in range(20):
    r = randrange(5, 9)
    print(r, end=" ")
print()

# randint(a, b) => [a, b]
print("2 és 14 között számok:")
for i in range(20):
    r = randint(2, 14)
    print(r, end=" ")
print()

# Páratlanok 1 és 20 között!
print("1 és 20 közötti páratlanok:")
for i in range(20):
    r = randrange(1, 20, 2)
    print(r, end=" ")
print()

# Kapcsolat a függvények között!
# randint(a, b) = randrange(a, b+1)