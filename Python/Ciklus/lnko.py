# lnko: legnagyobb közös osztó

# (4, 6) = 2
# (8, 12) = 4

a = int(input("a: "))
b = int(input("b: "))

c, d = a, b
while c != d:
    if c > d:
        c -= d
    else:
        d -= c
    # print(f"({c}, {d})")

print(f"({a}, {b}) = {c}")