# (a, b): legnagyobb közös osztó

a = int(input("a: "))
b = int(input("b: "))

r = a % b
while r != 0:
    a = b
    b = r
    r = a % b
oszto = b

print(f"({a}; {b}) = {b}")