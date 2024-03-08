'''
Készíts függvényt, amely
megadja, hogy egy listában melyik
számok a prímek!

A visszatérési érték a prímeket
tartalmazó lista legyen!
(Ha nincs prím, akkor üres lista.)

Ügyelj arra is, hogy az eredményben
csak egyedi számok legyenek!
'''

# Prímszám: 2 osztója van (1 és önmaga)
# Van-e olyan szám (ezen 2 számon kívül)
# amivel osztható?
# Ha van => nem prím
# különben => prím
def primE(n):
    if n == 1 or n == 0:
        return False
    n = abs(n)
    i = 2
    while i < n and not(n % i == 0):
        i += 1
    return not(i < n)

def eleme(elem, lista):
    i = 0
    while i < len(lista) and not(lista[i] == elem):
        i += 1
    return i < len(lista)

def primek(szamok):
    eredmeny = []
    for i in range(len(szamok)):
        if primE(szamok[i]) and not eleme(szamok[i], eredmeny):
            eredmeny.append(szamok[i])
    return eredmeny

# Tesztelés
def main():
    # print(primek([3, 11, 5, 3, 2, 3, 3, 2, 7]))
    print(primek([3, 11, 5, 3, 2, 3, 3, 2, 7]) == [3, 11, 5, 2, 7])
    print(primek([15, 101, 53, 119]) == [101, 53])
    print(primek([16, 32, 64, 128]) == [])

main()