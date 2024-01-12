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
# 6. Add meg az első olyan elemet, amely nagysága eléri a lista átlagát!
# Eléri: legalább akkora, mint az átlag
# Összegzés tétel
osszeg = 0
for i in range(n):
    osszeg += x[i]
atlag = osszeg / n

# Keresés => Kiválasztás
i = 0
while not(x[i] >= atlag):
    i += 1
print("6. Első szám ami eléri az átlagot:", x[i])

# F7
# 7. Monoton növekedő-e a lista?
# 7. Nem monoton növekvő!
# Eldöntés: Van-e elem, ami kisebb az előtte levőnél
# i = 0
# while i < n-1 and not(x[i] > x[i+1]):
#     i += 1

i = 1
while i < n and not(x[i] < x[i-1]):
    i += 1
if i < n:
    print("7. Nem monoton növekvő!")
else:
    print("7. Monoton növekvő!")

# F8
# Egyforma előjelű-e az összes eleme a listának?
# 8. Nem egyforma előjelű az összes elem!
# Igaz-e, hogy mindegyik elem ugyanolyan előjelű, mint az első?
# Eldöntés: Van-e olyan elem, ami más előjelű mint az első?
# x[0] > 0 and x[i] < 0 or x[0] < 0 and x[i] > 0
i = 0
while i < n and not(x[i] * x[0] < 0):
    i += 1
if i < n:
    print("8. Nem egyforma előjelűek!")
else:
    print("8. Mindegyik egyforma előjelű!")

# F9 


# F10
# 10. Van-e lokális maximum a listában? Ha igen, add meg az első helyét és értékét!
# Lokális maximum: nagyobb mindkét szomszédjánál.
# 10. Első lokális maximum helye: 3, értéke: 6.
i = 1
while i < n-1 and not(x[i] > x[i-1] and x[i] > x[i+1]):
    i += 1
if i < n-1:
    print("10. Első lokális maximum helye:", i+1 ,", értéke:", x[i])
else:
    print("10. Nincs lokális maximum.")

# F11


# F12

