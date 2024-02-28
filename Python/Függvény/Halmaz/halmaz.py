# Halmaz:
# 1. Elemeknek nincs sorrendje! (Listában van!)
# 2. Egy elem csak egyszer lehet benne! (Listában többször is!)

# lista1 = [1, 4, 3]
# lista2 = [1, 3, 4]
# halmaz1 = {1, 4, 3}
# halmaz2 = {1, 3, 4}

# Eldönti, hogy egy elem
# benne van-e egy listában
# Benne van: van olyan eleme, ami vele egyenlő!
# Eldöntés
def eleme(szam, lista):
    i = 0
    while i < len(lista) and not(lista[i] == szam):
        i += 1
    # if i < len(lista):
    #     return True
    # else:
    #     return False
    return i < len(lista)

# Kiválogatás
def egyediek(lista):
    eredmeny = []
    for i in range(len(lista)):
        if not eleme(lista[i], eredmeny):
            eredmeny.append(lista[i])
    return eredmeny

# Halmazkészítés tétel - egyediek kiválogatása
def main():
    lista = [3, 5, 3, 3, 2, 5, 2, 3]
    halmaz = egyediek(lista) # [3, 5, 2]
    print(halmaz)
    
main()