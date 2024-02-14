from random import random, randrange, randint

# 1. Csináljunk véletlen számokat
# a [5..12] intervallumon!

# Emlék:
# print(int(random()*8) + 5)

# Most:
print("Randrange:")
for i in range(20):
    r = randrange(5, 13)
    print(r, end=" ")
print()

# Vagy:
print("Randint:")
for i in range(20):
    r = randint(5, 12)
    print(r, end=" ")
    
print()
print("----------------------")

# 2. Csináljunk véletlen páratlan számokat
# a [5..12] intervallumon!
print("Randrange:")
for i in range(20):
    r = randrange(5, 13, 2)
    print(r, end=" ")
print()

# [5..12]-ről páros?
# [6..12]-ről páros => 6, 8, 10, 12
# 3, 4, 5, 6 = *2 = > 6, 8, 10, 12
print("Randint (párosak):")
for i in range(20):
    r = randint(3, 6) * 2
    print(r, end=" ")
print()

# [5..12]-ről páratlan?
# [5..11]-ről páratlan => 5, 7, 9, 11
# 3, 4, 5, 6 = *2 = > 6, 8, 10, 12
print("Randint (páratlanok):")
for i in range(20):
    r = randint(3, 6) * 2 - 1
    print(r, end=" ")
print()