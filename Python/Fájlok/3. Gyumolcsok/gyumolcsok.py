def beFajl(gyumolcsok, arak):
    fr = open("gyumolcsok.txt", "r", encoding="UTF-8")
    sor = fr.readline().strip() # "alma 367"
    while sor != "":
        darabolt = sor.split() # ["alma", "367"]
        gyumolcsok.append(darabolt[0])
        arak.append(int(darabolt[1]))
        sor = fr.readline().strip()
    fr.close()

def main():
    gyumolcsok, arak = [], []
    beFajl(gyumolcsok, arak)

main()