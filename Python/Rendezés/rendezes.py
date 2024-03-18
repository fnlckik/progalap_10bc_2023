from random import randint

# Emlék: változók cseréje
# seged = a
# a = b
# b = seged

# Másképp (python):
# a, b = b, a

# Megcseréli a kapott "x" lista
# "i"-edik és "j"-edik elemét!
def csere(x, i, j):
    x[i], x[j] = x[j], x[i]
    # seged = x[i]
    # x[i] = x[j]
    # x[j] = seged

# Megadja, hogy az "x" listában
# az "i"-edik elemtől kezdve
# melyik a legkisebb elem indexe!
def minimum_index(x, i):
    mini = i
    for j in range(i+1, len(x)):
        if x[j] < x[mini]:
            mini = j
    return mini

# Minimum kiválasztásos rendezés
def minkiv(x):
    n = len(x)
    for i in range(n):
        j = minimum_index(x, i)
        csere(x, i, j)

def feltolt(n):
    lista = []
    for i in range(n):
        r = randint(1, 9)
        lista.append(r)
    return lista

# Buborékos rendezést csinál a listán (javított)
# def buborekos(x):
#     n = len(x)
#     for i in range(n):
#         for j in range(n-1-i):
#             if x[j] > x[j+1]:
#                 csere(x, j, j+1)

def buborekos(x):
    n = len(x)
    for i in range(n):
        van_csere = False
        for j in range(n-1-i):
            if x[j] > x[j+1]:
                csere(x, j, j+1)
                van_csere = True
        if not van_csere:
            return None

def main():
    
    x = [5, 2, 7, 1, 2, 3]
    print("Eredeti:", x)
    buborekos(x)
    print("Rendezett:", x)

    x = feltolt(100)
    print("Random lista:", x)
    buborekos(x)
    print("Random rendezett:", x)

main()