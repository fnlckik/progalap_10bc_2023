n = int(input("n: "))

print("Fordított szám: ", end="")
while n > 0:
    utso = n % 10
    print(utso, end="")
    n = n // 10