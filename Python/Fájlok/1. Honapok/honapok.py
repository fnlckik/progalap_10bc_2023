def beKonzol(honapok):
    n = int(input())
    for i in range(n):
        sor = input()
        honapok.append(sor)

# "r": read -> olvasni fogunk a fájlból
# strip() => leszedi egy string szélén lévő white-space karaktereket
def beFajl(honapok):
    fr = open("honapok.txt", "r")
    n = int(fr.readline().strip())
    for i in range(n):
        sor = fr.readline().strip()
        honapok.append(sor)
    fr.close()

def main():
    honapok = []
    # beKonzol(honapok)
    beFajl(honapok)
    print(honapok)
    
main()