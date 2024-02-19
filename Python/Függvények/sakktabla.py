def sor(n, a, b):
    for i in range(n):
        if i % 2 == 0:
            print(a, end=" ")
        else:
            print(b, end=" ")
    print()

def main():
    n = int(input("Sorok száma: "))
    for i in range(n):
        if i % 2 == 0:
            sor(n, "X", "0")
        else:
            sor(n, "0", "X")


main()