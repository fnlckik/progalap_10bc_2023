# "Csak ott létezik"
# Lokális változó
def novel(x):
    x += 1

def novel2(x):
    return x + 1

def modosit(lista):
    # lista = [2, 3]
    lista[0] = 404
    lista.append(0)

# Globális változó
x = 5
novel(x)
print(x)

x = novel2(x)
print(x)

# --------------------------
# Ez is globális változó!
# Listák: memória címeket hordoznak magukban
lista = [5, 2, -3, 7]
modosit(lista)
print(lista)