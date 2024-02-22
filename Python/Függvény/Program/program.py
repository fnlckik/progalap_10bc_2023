# Tipikus python program felépítése számunkra

# Eljárás!
def beolvasas(szinek):
    n = int(input())
    for i in range(n):
        szin = input()
        szinek.append(szin)

def legrovidebb(szinek):
    mini = 0
    for i in range(1, len(szinek)):
        if len(szinek[i]) < len(szinek[mini]):
            mini = i
    return szinek[mini]

def kiiras(szin):
    print("A legrövidebb nevű szín:", szin)

# Most:
def main():
    szinek = []
    beolvasas(szinek)
    legrovidebb_szin = legrovidebb(szinek)
    kiiras(legrovidebb_szin)

main()