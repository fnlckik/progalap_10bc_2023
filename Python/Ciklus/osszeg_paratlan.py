# Első n darab páratlan szám összege!
# 2 => 1 + 3 = 4
# 3 => 1 + 3 + 5 = 9
# 4 => 1 + 3 + 5 + 7 = 16

# Beolvasás
n = int(input("n: "))

# Feldolgozás - Ádám
# osszeg = 0
# for i in range(1, n*2):
#     if i % 2 != 0:
#         osszeg += i

# Feldolgozás - Máté
'''
osszeg = 0
ertek = 1
# print(osszeg, end="")
for i in range(n):
    osszeg += ertek
    print(f"{osszeg-ertek} + {ertek} = {osszeg}")
    ertek += 2
print()
'''

# Feldolgozás - Kata
# osszeg = 0
# for i in range(1, n*2, 2):
#    osszeg += i


# Kiírás
print("Összeg:", osszeg)