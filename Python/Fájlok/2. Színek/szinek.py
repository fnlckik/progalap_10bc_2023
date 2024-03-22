# Kitekintés:
# sz = fr.readlines()
# print(sz)

def befajl(sz):
    fr = open("szinek.txt", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        sz.append(sor)
        sor = fr.readline().strip()
    fr.close()

def main():
    szinek = []
    befajl(szinek)
    print(szinek)

main()