# Van-e páros szám? => Eldöntés tétel

# Visszatérési értéke:
# I. Igaz, ha n páros
# II. Hamis, ha n páratlan
# def parosE(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
def parosE(n):
    return n % 2 == 0

# Visszatérési értéke:
# I. Ha van páros: az első páros
# II. Ha nincs páros: -1
# def elsoParos(x):
#     i = 0
#     while i < len(x) and not(parosE(x[i])):
#         i += 1
#     if i < len(x):
#         return x[i]
#     else:
#         return -1

# Visszatérési értéke:
# I. Igaz, ha van páros
# II. Hamis, ha nincs páros
def vanParos(x):
    i = 0
    while i < len(x) and not(parosE(x[i])):
        i += 1
    return i < len(x)
    # if i < len(x):
    #     return True
    # else:
    #     return False

def main():
    x = [5, 2, 3, 2, 2, 5, 7, 3]
    # print(elsoParos(x))
    print(vanParos(x))

main()