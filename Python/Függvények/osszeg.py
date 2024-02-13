# Visszatérési értéke: elemek összeg
# osszeg(lista)

# Benedek Bence
def osszeg(a):
    osszeg = 0
    for i in range(len(a)):
        osszeg += a[i]
    return osszeg

# Kulcsár Máté
def osszeg2(a):
    ...

print(osszeg([2, 5, -1])) #6
print(osszeg([3, -1])) #2
print(osszeg([1, 0, 2, 3, -1])) #5

print("-"*25)

print(osszeg2(2, 5, -1)) #6
print(osszeg2(3, -1)) #2
print(osszeg2(1, 0, 2, 3, -1)) #5
