n = int(input("n: "))

while n != 0:
    print(n, end=" ")
    if n % 2 == 0:
        n = n // 2
    else:
        n = n - 1