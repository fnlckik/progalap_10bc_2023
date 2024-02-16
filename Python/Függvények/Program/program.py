def beolvas(szinek):
    n = int(input())
    for i in range(n):
        szin = input()
        szinek.append(szin)
    
# Paraméter: ["piros", "lila", "barna", "fekete", "narancs"]
# Visszatérési érték: "lila"
def legrovidebbSzin(x):
    minind = 0
    minert = len(x[0])
    for i in range(len(x)):
        if len(x[i]) < minert:
            minert = len(x[i])
            minind = i
    return x[minind]

def kiir(szin):
    print("A legrövidebb szín:", szin)
    
def main():
    # Változók "létrehozása" + beolvas
    szinek = []
    beolvas(szinek)
    
    szin = legrovidebbSzin(szinek)
    
    kiir(szin)
    
main()