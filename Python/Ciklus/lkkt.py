# [a, b]: legkisebb közös többször

a = int(input("a: "))
b = int(input("b: "))

tobbszoros = a
while tobbszoros % b != 0:
    tobbszoros += a

print(f"[{a}, {b}] = {tobbszoros}")
