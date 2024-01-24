# Be
n = int(input())
bevetelek = []
for i in range(n):
    kassza = int(input())
    bevetelek.append(kassza)

# Feld
# FNL
# db = 0
# for i in range(1, n):
#     if bevetelek[i] > bevetelek[i-1]:
#         db += 1
# if bevetelek[0] > 0:
#     db += 1
# print(db)

eddigi = 0
db = 0
for i in range(n):
    if bevetelek[i] > eddigi:
        db += 1
        eddigi = bevetelek[i]
print(db)
