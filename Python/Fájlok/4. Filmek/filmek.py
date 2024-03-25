def beFajl(filmek, ertekelesek):
    fr = open("filmek.csv", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        darabolt = sor.split(";")
        filmek.append(darabolt[0])
        ertekelesek.append(float(darabolt[1]))
        sor = fr.readline().strip()
    fr.close()

def atlag(x):
    s = 0
    for i in range(len(x)):
        s += x[i]
    atl = round(s / len(x), 2)
    return atl

def main():
    filmek, ertekelesek = [], []
    beFajl(filmek, ertekelesek)
    print("Átlagos értékelés:", atlag(ertekelesek))

main()