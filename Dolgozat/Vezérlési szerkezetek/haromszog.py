# Beolvasás
alfa = int(input("Egyik szög: "))
gamma = int(input("Másik szög: "))

# Feldolgozás
beta = 180 - (alfa + gamma)
if gamma > 90:
    tipus = "tompaszögű"
elif gamma == 90:
    tipus = "derékszögű"
else:
    tipus = "hegyesszögű"

# Kiírás
print(f"A háromszög {tipus}, utolsó szöge {beta} fok.")
