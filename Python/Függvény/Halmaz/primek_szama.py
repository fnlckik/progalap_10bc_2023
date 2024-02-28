# Hány darab prímszám van a listában?

# Eldöntés:
# van-e neki 1-nél nagyobb osztója?
# Akkor prím, ha nem találtunk n-nél
# kisebb osztót neki!
def primE(n):
    i = 2
    while i < n and not(n % i == 0):
        i += 1
    # if i < n:
    #     return False
    # else:
    #     return True
    return not(i < n) and n != 1

# Megszámolás tétel
def primekSzama(x):
    ...

def main():
    x = [5, 3, 2, 8, 1]
    # db = primekSzama(x)    
    # print("Prímek száma:", db)
    print(primE(2))

main()