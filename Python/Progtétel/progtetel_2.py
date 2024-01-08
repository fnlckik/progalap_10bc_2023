x = [5, 1, 6, -3, 12, 8, 10, 29, 16, 6, 2, 11]
n = len(x)

# F0
# i = 0
# while i < n and x[i] != 6:
#     i += 1

i = 0
while i < n and not(x[i] == 6):
    i += 1
if i < n:
    print("0. Első 6-os sorszáma:", i+1)
else:
    print("0. Nincs 6-os a listában!")

# F1
# Add meg az első páros számot! Ha nincs a listában páros szám, akkor az „1. Nincs páros szám!” kerüljön a konzolra!
# x[i] % 2 != 0
# x[i] % 2 == 1
i = 0
while i < n and not(x[i] % 2 == 0):
    i += 1
if i < n:
    print("1. Első páros szám:", x[i])
else:
    print("1. Nincs páros szám!")

# F2
# Van-e a listában 10 és 20 közötti szám (a határokat is beleértve)? Ha igen, add meg a sorszámát!
# x[i] < 10 or x[i] > 20
i = 0
while i < n and not(x[i] >= 10 and x[i] <= 20):
    i += 1
if i < n:
    print("2. Első 10 és 20 közötti:", i+1)

# F3


# F4


# F5


# F6


# F7


# F8


# F9 


# F10


# F11


# F12

