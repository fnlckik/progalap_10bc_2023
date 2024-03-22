def beFajl(szinek):
    fr = open("szinek.txt", "r", encoding="UTF-8")
    sor = fr.readline().strip()
    while sor != "":
        szinek.append(sor)
        sor = fr.readline().strip()
    fr.close()

def main():
    szinek = []
    beFajl(szinek)
    print(szinek)
    
main()