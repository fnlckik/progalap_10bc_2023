x = [5, 1, 2, -6, 7, 7, 16, 2, 2, 32, -3, 5, 6]
n = len(x)

# F1 - Másolás tétel
# Másold át az elemeket egy másik listába!
# Ilyet soha nem! "y = x"
y = []
for i in range(n):
    y.append(x[i])
print("1. Másolt elemek:", y)

# F2
# Másold át az elemek négyzeteit egy másik listába!
negyzetek = []
for i in range(n):
    aktualis = x[i]*x[i]
    negyzetek.append(aktualis)
print("2. Négyzetek:", negyzetek)

# F3 - Kiválogatás tétel
# Válogasd ki a 10 alatti elemeket egy másik listába!
alattiak = []
for i in range(n):
    if x[i] < 10:
        alattiak.append(x[i])
print("3. Tíz alattiak:", alattiak)        

# F4
# Válogasd ki a negatív elemek indexeit egy másik listába!
negativak = []
for i in range(n):
    if x[i] < 0:
        negativak.append(i)
print("4. Negatívak indexei:", negativak)

# Kiírás
print("Negatívak sorszámai:", end=" ")
for index in negativak:
    print(index + 1, end=" ")
print()
print("Negatívak:", end=" ")
for index in negativak:
    print(x[index], end=" ")
print()

# F5 - Szétválogatás tétel
# T tulajdonságúak egyik listába
# nem T tulajdonságúak másik listába
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

