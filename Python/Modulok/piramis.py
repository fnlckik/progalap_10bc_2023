n = int(input("Magasság: "))

for i in range(1, n+1):
    for j in range(n-i): # (2*n-2*i) // 2
        print(" ", end="")
    for j in range(i):
        print(j+1, end=" ")
    for j in range(n-i):
        print(" ", end="")
    print()
