# Lokális változó (helyi, csak itt "látható")
# Csak itt létezik a függvényen belül
# "Kívülre" nem látszódik
# Ennek az "x" lokális változónak a
# novel() függvény a hatóköre => scope
def novel(x):
    x += 1
    print("Függvényen belül:", x)
    
# Globális változó
x = 5
novel(x)
print("Függvény után:", x)

# ------------------------------------
def modosit(x):
    # x = [1, 4]
    x[0] = 404
    x.append(112)

lista = [5, 2, 3]
modosit(lista)
print(lista) # [404, 2, 3, 112]
