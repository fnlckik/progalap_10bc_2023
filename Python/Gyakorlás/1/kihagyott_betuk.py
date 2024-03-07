'''
Készíts függvényt betuk(s) néven, amely
paraméterként kap egy szöveg és a szöveg minden
szóköztől különböző betűjét 20% valószínűséggel kicseréli "_" jelre!
A szóközöket biztosan megtartja!

Pl.: betuk("abc") lehetséges értékei:
"abc", "ab_", "a_c", "_bc", "__c", "_b_", "a__", "___"
'''

from random import randint

def betuk(s):
    eredmeny = ""
    for i in range(len(s)):
        r = randint(1, 5)
        if r == 1 and s[i] != " ":
            eredmeny += "_"
        else:
            eredmeny += s[i]
    return eredmeny

def main():
    print(betuk("Szerencsekerék"))
    print(betuk("Igen"))
    print(betuk("Még nyílnak a völgyben a kerti virágok"))
    print(betuk("Volt egyszer egy óriási kisegér"))

main()