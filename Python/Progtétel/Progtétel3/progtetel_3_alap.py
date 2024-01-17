x = [5, 1, 2, -6, 7, 7, 16, 2, 2, 32, -3, 5, 6]
n = len(x)

# F1 - Másolás tétel
# Másold át az elemeket egy másik listába!
y = []
for i in range(n):
    y.append(x[i])
print("1. Másolt lista:", y)

# F2
# Másold át az elemek négyzeteit egy másik listába!
negyzetek = []
for i in range(n):
    aktualis = x[i]*x[i]
    negyzetek.append(aktualis)
print("2. Négyzetek:", negyzetek)

# F3 - Kiválogatás tétel
# Válogasd ki a 10 alatti elemeket egy másik listába!
tizalattiak = []
for i in range(n):
    if x[i] < 10:
        tizalattiak.append(x[i])
print("3. Tíz alattiak:", tizalattiak)

# F4
# Válogasd ki a negatív elemek indexeit egy másik listába!
negativak = []
for i in range(n):
    if x[i] < 0:
        negativak.append(i)
print("4. Negatívak indexei:", negativak)

rosszmo = []
for i in range(n):
    if x[i] < 0:
        rosszmo.append(x[i])
print("Negatívak értékei:", rosszmo)

ertekek = []
m = len(negativak) # 2
for i in range(m):
    index = negativak[i] # 3, 10
    ertekek.append(x[index])
    # ertekek.append(x[negativak[i]])
print("Negatívak értékei:", ertekek)

# F5 - Szétválogatás tétel
# Válogasd szét a páros és a páratlan elemeket!
parosak = []
paratlanok = []
for i in range(n):
    if x[i] % 2 == 0:
        parosak.append(x[i])
    else:
        paratlanok.append(x[i])
print("5. Párosak és páratlanok")
print("Párosak:", parosak)
print("Páratlanok:", paratlanok)

# F6
# Válogasd ki a lokális minimumok indexeit!
# Lokális minimum: közbülső elem, aki szomszédainál kisebb
# szomszédainál kisebb: x[i] < x[i-1] and x[i] < x[i+1]

lokalminek = []
for i in range(1, n-1):
    if x[i] < x[i-1] and x[i] < x[i+1]:
        lokalminek.append(i)
print("6. Lokális minimumok:", lokalminek)

# F7
# Válogasd szét a lista indexeit az alapján,
# hogy adott helyen az érték nő / csökken / állandó!
novekedesek = []
csokkenesek = []
allandok = []
for i in range(1, n): # 1-től n-i-ig
    if x[i] > x[i-1]:
        novekedesek.append(i)
    elif x[i] < x[i-1]:
        csokkenesek.append(i)
    else:
        allandok.append(i)
print("7. Elemek növekedése")
print("Növekedők:", novekedesek)
print("Csökkenők:", csokkenesek)
print("Állandók:", allandok)
