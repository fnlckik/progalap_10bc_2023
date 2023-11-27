# lkkt: legkisebb közös többszörös

# [4, 6] = 12
# [6, 8] = 24

a = int(input("a: "))
b = int(input("b: "))

c = a
while c % b != 0:
    c += a

print(f"[{a}, {b}] = {c}")