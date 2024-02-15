# 4,5-től: 60000
# 4-től: 42000
# 3,5-től: 28000
# 3-tól: 16000
# alatta: 8000

def osztondij(atlag):
    if atlag >= 4.5:
        return 60000
    elif atlag >= 4:
        return 42000
    elif atlag >= 3.5:
        return 28000
    elif atlag >= 3:
        return 16000
    else:
        return 8000
    
# def osztondij(atlag):
#     if atlag >= 4.5:
#         dij = 60000
#     elif atlag >= 4:
#         dij = 42000
#     elif atlag >= 3.5:
#         dij = 28000
#     elif atlag >= 3:
#         dij = 16000
#     else:
#         dij = 8000
#     return dij

print("4,8 =>", osztondij(4.8))   # 60000
print("2,9 =>", osztondij(2.9))   # 8000
print("3,77 =>", osztondij(3.77)) # 28000
print("3,13 =>", osztondij(3.13)) # 16000

# print("-"*25)
# atlag = 4.8
# if atlag >= 4.5:
#     print(60000)
# elif atlag >= 4:
#     print(42000)
# elif atlag >= 3.5:
#     print(28000)
# elif atlag >= 3:
#     print(16000)
# else:
#     print(8000)

# atlag = 2.9
# if atlag >= 4.5:
#     print(60000)
# elif atlag >= 4:
#     print(42000)
# elif atlag >= 3.5:
#     print(28000)
# elif atlag >= 3:
#     print(16000)
# else:
#     print(8000)

# atlag = 3.77
# if atlag >= 4.5:
#     print(60000)
# elif atlag >= 4:
#     print(42000)
# elif atlag >= 3.5:
#     print(28000)
# elif atlag >= 3:
#     print(16000)
# else:
#     print(8000)

# atlag = 3.13
# if atlag >= 4.5:
#     print(60000)
# elif atlag >= 4:
#     print(42000)
# elif atlag >= 3.5:
#     print(28000)
# elif atlag >= 3:
#     print(16000)
# else:
#     print(8000)