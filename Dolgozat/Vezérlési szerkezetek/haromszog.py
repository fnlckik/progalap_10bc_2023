# Beolvasás
a = int(input("Egyik szög: "))
b = int(input("Másik szög: "))

# Feldolgozás
szog = 180 - (a + b)
if b < 90:
    tipus = "hegyesszögű"
elif b == 90:
    tipus = "derékszögű"
else:
    tipus = "tompaszögű"

# Kiírás
print(f"A háromszög {tipus}, utolsó szöge {szog} fok.")