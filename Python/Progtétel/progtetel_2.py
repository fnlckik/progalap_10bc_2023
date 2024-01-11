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
# 3. Található-e 3-mal osztható páratlan szám? Amennyiben igen, add meg az elsőt!
# 3. Első 3-mal osztható páratlan: -3
i = 0
while i < n and not(x[i] % 3 == 0 and x[i] % 2 == 1):
    i += 1
if i < n:
    print("3. Első 3-mal osztható páratlan:", x[i])    

# F4
# 4. Osztható-e valamelyik szám 4-gyel? Ha igen, add meg az utolsót!
# 4. Utolsó 4-gyel oszható: 16
# "Klasszikus megoldás"
i = n-1
while i >= 0 and not(x[i] % 4 == 0):
    i -= 1
if i >= 0:
    print("4. Utolsó 4-gyel oszható:", x[i])
else:
    print("4. Nincs 4-gyel osztható!")

# i = 0
# while i < n and not(x[n-1-i] % 4 == 0):
#     i += 1
# if i < n:
#     print("4. Utolsó 4-gyel oszható:", x[n-1-i])
# else:
#     print("4. Nincs 4-gyel osztható!")

# F5
# 5. Igaz-e, hogy a lista első eleme a legkisebb?
# 5. Nem az első a legkisebb!
# Eldöntés: Van-e kisebb az első elemnél?
i = 0
while i < n and not(x[i] < x[0]):
    i += 1
if i < n:
    print("5. Nem az első a legkisebb!")
else:
    print("5. Az első a legkisebb!")

# F6


# F7
# 7. Monoton növekedő-e a lista?
# 7. Nem monoton növekvő!


# F8


# F9 


# F10


# F11


# F12

