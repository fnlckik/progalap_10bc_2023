from math import pi, sqrt as gyok
from random import randint

def generalas(oldalak):
    a = randint(1, 100)
    b = randint(a, 100)
    c = gyok(oldalak[0] ** 2 + oldalak[1] ** 2)
    oldalak.append(a)
    oldalak.append(b)
    oldalak.append(round(c, 2))
    
def haromszog(a, b):
    return a * b / 2

def arany(t1, t2):
    return round(t1 / t2 * 100, 2)

def kor(r):
    return pi * r ** 2

def main():
    x = []
    generalas(x)
    ht = haromszog(x[0], x[1])
    kt = kor(x[2] / 2)
    print(f"Arány: {arany(ht, kt)}%")

main()
