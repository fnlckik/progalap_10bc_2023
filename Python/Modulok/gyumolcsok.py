from random import randint, choice

x = ["alma", "korte", "barack", "szilva", "meggy", "eper", "banan"]
n = len(x)

print("Gondolkodva:")
for i in range(20):
    r = randint(0, n-1)
    gyumolcs = x[r]
    print(f"{i+1}. {gyumolcs}")
print()

print("Choice:")
for i in range(20):
    gyumolcs = choice(x)
    print(f"{i+1}. {gyumolcs}")