# Tipikus python program felépítése számunkra

# Beolvasas
n = int(input())
szinek = []
for i in range(n):
    szin = input()
    szinek.append(szin)

# Feldolgozas - min kiválasztás tétel
mini = 0
for i in range(1, n):
    if len(szinek[i]) < len(szinek[mini]):
        mini = i
legrovidebb_szin = szinek[mini]

# Kiiras
print("A legrövidebb nevű szín:", legrovidebb_szin)

# Most:
# beolvasas()
# feldolgozas()
# kiiras()
