n = int(input("Osztályzat: "))

helyes = 1 <= n and n <= 20
if not(helyes):
    print("Nem jó osztályzat!")
elif n <= 10:
    print("Bukott!")
else:
    print("Nem bukott!")

# nemhelyes = n < 1 or n > 20
# if nemhelyes:
#     print("Nem jó osztályzat!")

# Python esetén!!!
# a <= b <= c jelentése: a<=b and b<=c
# helyes = 1 <= n <= 20
# if not(helyes):
#     print("Nem jó osztályzat!")

