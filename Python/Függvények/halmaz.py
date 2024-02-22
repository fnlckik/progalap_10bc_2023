# Halmaz:
# 1. Elemek sorrendje nem számít
# 2. Minden elem egyedi (egyszer fordulhat elő)

# Csináljunk belőle halmazt!
# x = {5, 2, 3, 7}
# Válogassuk ki az elemeket!
# Minden elem egyedi legyen!

# Visszatérési érték:
# I. Igaz, ha "elem" benne van a "halmaz"-ban
# II. Hamis, ha "elem" nincs benne a "halmaz"-ban
# Eldöntés tétel!
def eleme(elem, halmaz):
    i = 0
    while i < len(halmaz) and not(halmaz[i] == elem):
        i += 1
    return i < len(halmaz)
    # if i < len(halmaz):
    #     return True
    # else:
    #     return False

def main():
    x = [5, 2, 3, 2, 2, 5, 7, 3]
    y = []
    for i in range(len(x)):
        if not eleme(x[i], y):
            y.append(x[i])
    print(y)

main()