def eleme(e, halmaz):
    n = len(halmaz)
    i = 0
    while i < n and not(halmaz[i] == e):
        i += 1
    return i < n

# Menjünk végig az "a" halmazon
# Válogassuk ki azon elemeket
# amik benne vannak a "b"-ben is!
# Kiválogatás + Eldöntés
def metszet(a, b):
    eredmeny = []
    for i in range(len(a)):
        if eleme(a[i], b):
            eredmeny.append(a[i])
    return eredmeny

# Az első halmazból minden kell!
# A másikból azok, amiket még nem vettünk ki!
def unio(a, b):
    eredmeny = []
    # Kell minden az A-ból!
    for i in range(len(a)):
        eredmeny.append(a[i])
    # Kell B-ből az, ami nincs az A-ban!
    for i in range(len(b)):
        if not eleme(b[i], a):
            eredmeny.append(b[i])
    return eredmeny

# Azon elem, amik "a"-ban benne vannak
# de "b"-ben nincsenek!
def kulonbseg(a, b):
    eredmeny = []
    for i in range(len(a)):
        if not eleme(a[i], b):
            eredmeny.append(a[i])
    return eredmeny

def main():
    a = [3, 5, 2, -7, 13, 8] #6 elem
    b = [1, -4, 2, 8, 14] #5 elem
    # Halmazok
    print("A:", a)
    print("B:", b)
    
    # Metszet: [2, 8]
    m = metszet(a, b)
    print("Metszet:", m)
    
    # Unio: [3, 5, 2, -7, 13, 8, 1, -4, 14]
    u = unio(a, b)
    print("Unio:", u)
    
    # Különbség: [3, 5, -7, 13]
    k = kulonbseg(a, b)
    print("Különbség:", k)
    
main()