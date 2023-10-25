n = int(input("Osztályzat: "))

# Osztályzat helyességének tesztje
if n < 1 or n > 20:
    print("Rossz osztályzat!")
    exit()

# Bukás tesztelése
if n <= 10:
    print("Bukott!")
else:
    print("Nem bukott!")