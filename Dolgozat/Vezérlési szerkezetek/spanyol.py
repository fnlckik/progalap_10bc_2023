kezd = int(input("Kezdeti szint: "))
telj = int(input("Teljesített szintek: "))

for i in range(kezd+1, kezd+telj+1):
    print(f"Gratulálunk a(z) {i}. szinthez, jutalmad {i*5} drágakő!")