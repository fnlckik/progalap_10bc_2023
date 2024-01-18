# szamok = [2, 7, 4, 12, -3, 5]

# Olvass be és tárolj el
# n darab számot egy listába!
n = int(input())
szamok = []
for i in range(n):
    bemenet = int(input())
    szamok.append(bemenet)
print(szamok)

# Összeg
s = 0
for i in range(n):
    s += szamok[i]
print(s)

# Négyzetek
y = []
for i in range(n):
    negyzet = szamok[i]*szamok[i]
    y.append(negyzet)
print(y)
