# Pl.: n = 5
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

def sor(n):
    for i in range(1, n+1):
        print(i, end=" ")
    print()

def main():
    n = int(input("Sorok száma: "))
    for i in range(1, n+1):
        sor(i)

main()