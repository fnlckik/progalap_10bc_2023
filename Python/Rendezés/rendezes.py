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

def rendez(x):
    n = len(x)
    for i in range(n):
        j = minimum_index(x, i)
        csere(x, i, j)

def main():
    x = [5, 2, 7, 1, 2, 3]

    print("Eredeti:", x)
    rendez(x)
    print("Rendezett:", x)

    

main()