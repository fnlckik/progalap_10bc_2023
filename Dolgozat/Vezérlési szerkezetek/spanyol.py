kezdeti = int(input("Kezdeti szint: "))
teljesitett = int(input("Teljesített szint: "))

# utolso = kezdeti + teljesitett
# for i in range(kezdeti+1, utolso+1):
#     print(f"Gratulálunk a(z) {i}. szinthez, jutalmad {i*5} drágakő!")

# szint = kezdeti
# for i in range(teljesitett):
#     szint += 1
#     print(f"Gratulálunk a(z) {szint}. szinthez, jutalmad {szint*5} drágakő!")

szint = kezdeti
utolso = kezdeti + teljesitett
while szint < utolso:
    szint += 1
    print(f"Gratulálunk a(z) {szint}. szinthez, jutalmad {szint*5} drágakő!")
