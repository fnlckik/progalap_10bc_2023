# Beolvasni + mennyi az átlagár?

def befajl(gyumolcsok, arak):
    fr = open("gyumolcsok.txt", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        adatok = sor.split()
        gyumolcsok.append(adatok[0])
        arak.append(int(adatok[1]))
        sor = fr.readline().strip()
    fr.close()

def main():
    gyumolcsok, arak = [], []
    befajl(gyumolcsok, arak)
    print(gyumolcsok)
    print(arak)
    # print("Átlagos ár:", atlag(arak))

main()