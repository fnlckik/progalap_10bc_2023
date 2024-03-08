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

# Tesztelés
def main():
    print(primek([5, 1, 26, 17, 38]) == [5, 17])
    print(primek([3, 11, 5, 3, 2, 3, 3, 2, 7]) == [3, 11, 5, 2, 7])
    print(primek([15, 101, 53, 119]) == [101, 53])
    print(primek([16, 32, 64, 128]) == [])

main()