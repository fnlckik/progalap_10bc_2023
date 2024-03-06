'''
Készíts függvényt egyedi_hosszuak(x) néven, amely
megadja az x lista azon elemeit,
amelyek előtt nincs velük azonos hosszú elem!

Paraméterek:
x: szövegeket tartalmazó lista

Visszatérési érték:
Egy lista a megfelelő (egyedi) elemekkel!
'''

# Függvény:
# Igaz, ha van "n" hosszú szó a listában
# Hamis, ha nincs "n" hosszú szó a listában
def van_ilyen_hossz(n, lista):
    ...

def egyedi_hosszuak(szavak):
    egyediek = []
    for i in range(len(szavak)):
        if not van_ilyen_hossz(len(szavak[i]), egyediek):
            egyediek.append(szavak[i])
    return egyediek

def main():
    print(egyedi_hosszuak(["alma", "banan", "korte", "barack"]) == ["alma", "banan", "barack"])
    print(egyedi_hosszuak(["piros", "feher", "zold", "barna", "lila"]) == ["piros", "zold"])
    print(egyedi_hosszuak(["abc", "aab", "abba", "baba"]) == ["abc", "abba"])
    print(egyedi_hosszuak(["alma", "banan", "korte", "barack"]))
    print(egyedi_hosszuak(["piros", "feher", "zold", "barna", "lila"]))
    print(egyedi_hosszuak(["abc", "aab", "abba", "baba"]))

main()