def terulet(a, b = 0):
    if b == 0:
        b = a
    return a * b

print(terulet(3, 7)) # 3 és 7 oldalú téglalap
print(terulet(5)) # 5 oldalú négyzet