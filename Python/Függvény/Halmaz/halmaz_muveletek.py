# Halmaz műveletek:
# Komplementer: ???
# Metszet: közös elemek
# Unio: egyesítés (összes elem)
# Különbség: egyikben benne, másikban nincs

# Eldönti, hogy "e" benne van-e
# az "x" listában.
def bennevan(e, x):
    n = len(x)
    i = 0
    while i < n and not(x[i] == e):
        i += 1
    return i < n

# Válogassuk ki azon elemeket
# az A-ból, amelyek B-ben is benne vannak
def metszet(a, b):
    eredmeny = []
    for i in range(len(a)):
        if bennevan(a[i], b):
            eredmeny.append(a[i])
    return eredmeny

# Unio:
# Vegyük ki az A-ból az összes elemet!
# Vegyük ki azokat B-ből amik nem voltak az A-ban
def unio(a, b):
    eredmeny = []
    for i in range(len(a)):
        eredmeny.append(a[i])
    for i in range(len(b)):
        if not bennevan(b[i], a):
            eredmeny.append(b[i])
    return eredmeny

# Különbség:
# Ami A-ban benne van, de B-ben nincs
def kulonbseg(a, b):
    eredmeny = []
    for i in range(len(a)):
        if not bennevan(a[i], b):
            eredmeny.append(a[i])
    return eredmeny

def szimm_diff(a, b):
    u = unio(a, b)
    m = metszet(a, b)
    return kulonbseg(u, m)

def szimm_diff2(a, b):
    k1 = kulonbseg(a, b)
    k2 = kulonbseg(b, a)
    return unio(k1, k2)

def main():
    a = [2, 7, 1, 5, 3]
    b = [1, 6, 8, 7]

    print("A:", a)
    print("B:", b)

    # m = [7, 1]
    m = metszet(a, b)
    print("Metszet:", m)

    # m2 = metszet(b, a)
    # print("Metszet2:", m2)
    
    # u = [2, 7, 1, 5, 3, 6, 8]
    u = unio(a, b)
    print("Unio:", u)
    
    # u2 = unio(b, a)
    # print("Unio2:", u2)
    
    # A-ban benne van, de B-ben nincs!
    # k1 = [2, 5, 3]
    k1 = kulonbseg(a, b)
    print("Különbség (A\B):", k1)
    
    # k2 = [6, 8]
    k2 = kulonbseg(b, a)
    print("Különbség (B\A):", k2)

    # Szimmetrikus differencia
    sz = szimm_diff(a, b)
    print("Szimm. diff.:", sz)

    sz2 = szimm_diff2(a, b)
    print("Szimm. diff.:", sz2)

main()