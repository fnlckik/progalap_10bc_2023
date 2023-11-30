# lnko: legnagyobb közös osztó

# (4, 6) = 2
# (8, 12) = 4

a = int(input("a: "))
b = int(input("b: "))

eredetA, eredetB = a, b

r = a % b
while r != 0:
    a = b
    b = r
    r = a % b

print(f"({eredetA}, {eredetB}) = {b}")