n = int(input("n: "))

# Dr. Stefkovics processzor úr
# osszeg = 0
# pozitivE = True
# for i in range(1, n+1):
#     if pozitivE:
#         osszeg += i*i
#     else:
#         osszeg += i*i*(-1)
#     pozitivE = not pozitivE

# Balázs Espanol
# osszeg = 0
# for i in range(1, n+1):
#     if i % 2 == 1:
#         osszeg += i*i
#     else:
#         osszeg -= i*i

# Mr. Magyar verseny
osszeg = 0
for i in range(1, n+1):
    aktualis = i*i
    if aktualis % 2 == 0:
        aktualis *= (-1)
    osszeg += aktualis

print("Négyzetösszeg:", osszeg)