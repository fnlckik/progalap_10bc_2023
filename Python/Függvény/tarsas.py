from random import randint

def mezo(kezdo):
    # d = randrange(1, 7)
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    # if d1 > d2:
    #     return kezdo + d1
    # elif d2 > d1:
    #     return kezdo + d2
    # else:
    #     return kezdo + d1 * 2
    if d1 == d2:
        return kezdo + d1 + d2
    elif d1 > d2:
        return kezdo + d1
    else:
        return kezdo + d2

print(mezo(5))
# mezo(1) => 3; 4; 5; 6; 7; 9; 11; 13
# 3 => 1;1 vagy 1;2 vagy 2;1 => 3db
# 4 => 1;3 vagy 3;1 vagy 2;3 vagy 3;2 => 4db
# 5 => 2;2 vagy 1;4 vagy 2;4 vagy 3;4 vagy 4;1 vagy 4;2 vagy 4;3 => 7db
