# Be
n = int(input())
bevetelek = []
for i in range(n):
    x = int(input())
    bevetelek.append(x)

# Feld. - Megszámolás
db = 0
for i in range(1, n):
    if bevetelek[i] > bevetelek[i-1]:
        db += 1
if bevetelek[0] != 0:
    db += 1

# Ki
print(db)
