n = int(input("n: ")) # 1234

print("Fordított szám: ", end="")
while n > 0:
    utso = n % 10 # 4
    n = n // 10 # 123
    print(utso, end="")
