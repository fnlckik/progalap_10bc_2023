def csere(x, i, j):
    x[i], x[j] = x[j], x[i]

# Buborékos rendezés
# Rendezi az "x" és "y" listák elemeit (párhuzamosan)
# az "x" szerint növekvő sorrendben!
def rendez(x, y):
    n = len(x)
    for i in range(n):
        for j in range(n-1-i):
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                y[j], y[j+1] = y[j+1], y[j]

def main():
    nevek = ["Robi", "Laci", "Anna",  "Dani", "Ricsi", "Marci"]
    magassagok = [175, 142, 150, 158, 172, 175]
    n = len(nevek)

    # F1 - Adjuk meg a névsort!
    # Feltehető, hogy nincs ékezet a nevekben!
    rendez(nevek, magassagok)
    print("1. Névsor:", nevek)

    # Megjegyzes:
    # chr(65) == "A"
    # ord("A") == 65
    # Gond: ord("á") == 225

    # F2 - Adjuk meg a tornasort (nevek)!
    # (Magasság szerinti növekvő sorrend.)
    rendez(magassagok, nevek)
    print("2. Tornasor:")
    print("   Nevek:", nevek)
    print("   Magasságok:", magassagok)

    # F3 - Egyetlen rendezési függvényt használjunk! - Kesz

    # F4 - Azonos magasságok esetén a névsor alapján rendezzünk!
    
    # F5 - Adjuk meg, hogy ki áll a tornasor közepén (medián)!
    print("5. A tornasor közepe: ", end="")


main()