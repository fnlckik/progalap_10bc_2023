x = [3, 12, -4, 7, 10, 8]
n = len(x)

# A
# s = 0
# for i in range(n):
#     if x[i] % 2 == 0:
#         s += x[i]
# print(s)

s = 0
for elem in x:
    if elem % 2 == 0:
        s += elem
print(s)

# db = 0
# for i in range(n):
#     if x[i] > x[0]:
#         db += 1
# print(db)

db = 0
for elem in x:
    if elem > x[0]:
        db += 1
print(db)

# B
db = 0
for i in range(n):
    if x[i] > -10 and x[i] < 10:
        db += 1
print(db)

szorzat = 1
for i in range(n):
    if x[i] > 0:
        szorzat *= x[i]
print(szorzat)
