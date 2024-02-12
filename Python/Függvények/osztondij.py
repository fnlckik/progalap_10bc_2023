# 4.5-től: 57000
# 4-től: 42000
# 3.5-től: 25000
# 3-tól: 8000
# Egyébként: 0

def osztondij(atlag):
    if atlag >= 4.5:
        return 57000
    elif atlag >= 4:
        return 42000
    elif atlag >= 3.5:
        return 25000
    elif atlag >= 3:
        return 8000
    else:
        return 0

print("4,5 =>", osztondij(4.5)) #57000
print("2,7 =>", osztondij(2.7)) #0
print("3,2 =>", osztondij(3.2)) #8000
print("4 =>", osztondij(4)) #42000