# Eldöntés
def bennevan(elem, lista):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)

# Kiválogatás + eldöntés
def kivalogat(lista):
    eredmeny = []
    for i in range(len(lista)):
        if lista[i] > 0 and not bennevan(lista[i], eredmeny):
            eredmeny.append(lista[i])
    return eredmeny

def main():
    print(kivalogat([5, 0, -1, 2, 2, 5])) # [5, 2]
    
main()