a = int(input("a: "))
b = int(input("b: "))

eredetA, eredetB = a, b

r = a % b
while r != 0:
    a = b
    b = r
    r = a % b

lnko = b
# Áll: (a;b) * [a;b] = a*b
lkkt = eredetA * eredetB // lnko

print(f"[{eredetA}, {eredetB}] = {lkkt}")