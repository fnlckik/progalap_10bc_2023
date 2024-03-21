def bekonzol(h):
    n = int(input())
    for i in range(n):
        honap = input()
        h.append(honap)

# Megnyitom a "honapok.txt" fájlt
# olvasási (read) módban!
# fr: file reader (fájl olvasó)
def befajl(h):
    fr = open("honapok.txt", "r")
    n = int(fr.readline())
    for i in range(n):
        honap = fr.readline().strip()
        h.append(honap)
    fr.close()

def main():
    honapok = []
    befajl(honapok)
    print(honapok)

main()