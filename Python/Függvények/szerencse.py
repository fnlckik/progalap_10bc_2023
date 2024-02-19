from random import randint

# 100 tét
# Mi történik várhatóan? (6-szor dobva)
# Tétek: 600 Ft
# 0 + 0 + 0 + 50 + 50 + 500 => 600 Ft
# Várható nyeremény: 0 Ft
def nyeremeny(x):
    r = randint(1, 6)
    if r == 6:
        return x * 5
    elif r >= 4:
        return x / 2
    else:
        return 0
    # if r == 1 or r == 2 or r == 3:
    #     return 0
    # elif r == 4 or r == 5:
    #     return x / 2
    # else:
    #     return x * 5
    
tet = 10 # Ft
n = 100 # dobasok szama
penz = 50
print("Kezdetben:", penz)
i = 0
while i < n and penz > 0:
    x = nyeremeny(tet)
    penz = penz - tet + x
    i += 1
    # print(penz)
if penz <= 0:
    print("Gond van:", penz)
print("Végén:", penz)