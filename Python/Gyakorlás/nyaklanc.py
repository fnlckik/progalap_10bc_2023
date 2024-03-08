'''
Sára nyakláncot készít piros, sárga és kék
színű gyöngyökből.

Egyetlen fontos szabály van:
piros gyöngyöt nem követhet kék!

Készíts függvényt nyaklanc(n) néven,
amely visszatérési értéke egy n hosszú
szöveg, amely P, S és K karakterekből áll
a fenti szabálynak megfelelően!

Pl.:
nyaklanc(2) lehetséges értékei:
"PP", "PS",
"SS", "SK", "SP"
"KK", "KS",

nyaklanc(3) lehet például:
Lehet: "PSK", "KPS"
Nem lehet: "KSP"

Vigyázat: nem csak "PK", de "KP" sem jó,
mert a nyaklánc két végét össze kell kötni!
'''

from random import randint

def sorsolas(szinek):
    # szinek = ["P", "S", "K"]
    r = randint(0, len(szinek)-1)
    # if r == 0:
    #     return "P"
    # elif r == 1:
    #     return "S"
    # else:
    #     return "K"
    return szinek[r]

def nyaklanc(n):
    eredmeny = sorsolas(["P", "S", "K"])
    for i in range(1, n):
        gyongy = sorsolas(["P", "S", "K"])
        if eredmeny[i-1] == "P":
            gyongy = sorsolas(["P", "S"])
        if i == n-1 and eredmeny[0] == "K":
            gyongy = sorsolas(["S", "K"])
        if i == n-1 and eredmeny[0] == "K" and eredmeny[i-1] == "P":
            gyongy = "S"
        eredmeny += gyongy
    return eredmeny

# Tesztelés
def main():
    print(nyaklanc(2))
    print(nyaklanc(3))
    print(nyaklanc(7))
    print(nyaklanc(15))

main()