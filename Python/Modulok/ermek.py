from random import randint
n = int(input("Dobások száma: "))

irasDb = 0
fejDb = 0
for i in range(n):
    r = randint(1, 2)
    if r == 1:
        print("F", end=" ")
        fejDb += 1
    else:
        print("I", end=" ")
        irasDb += 1
print()

# Gyakoriság
print("Fejek száma:", fejDb)
print("Írások száma:", irasDb)

# Relatív gyakoriság
print(f"Fejek aránya: {round(fejDb / n * 100, 5)}%")
print(f"Írások aránya: {round(irasDb / n * 100, 5)}%")
