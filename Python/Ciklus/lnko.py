# (a, b): legnagyobb közös osztó

a = int(input("a: "))
b = int(input("b: "))

while a != b:
    # print(f"({a}; {b})")
    if a > b:
        a -= b
    else:
        b -= a
oszto = a # oszto = b

print(f"({a}; {b}) = {oszto}")