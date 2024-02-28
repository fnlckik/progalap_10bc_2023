import math
from random import randint

def generalas(oldalak): 
    b1 = randint(1,100)
    b2 = randint(b1, 100)
    oldalak.append(b1)
    oldalak.append(b2)
    # b2 = randint(1,100)
    # if b1 > b2:
    #     oldalak.append(b2)
    #     oldalak.append(b1)
    # else:
    #     oldalak.append(b1)
    #     oldalak.append(b2)
    atfogo = round(math.sqrt((b1**2)+(b2**2)),2)    
    oldalak.append(atfogo)
    print(oldalak)

def haromszog(a,b):
    return a*b/2

def kor(r):
    return r**2*math.pi

def arany(t1,t2):
    return round(t1/t2*100,2)

def main():
    x = []
    generalas(x)
    ht = haromszog(x[0], x[1])
    kt = kor(x[2] / 2)
    print(f"Arány: {arany(ht, kt)}%")
main()
