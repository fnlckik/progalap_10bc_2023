def sorkiiras(sor):
    for i in range(len(sor)):
        print(sor[i], end=" ")
    print()

def szampiramis(n):
    sor = []
    for i in range(1, n+1):
        sor.append(i)
        sorkiiras(sor)
    
def main():
    n = int(input("Sorok száma: "))
    szampiramis(n)

main()