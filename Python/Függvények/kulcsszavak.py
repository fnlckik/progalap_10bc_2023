# vnev = ""
# Alapértelmezett értéket kapott a vnev
# Ilyenkor a positional argumentumok után kell jönnie!
def koszon(forma, knev, vnev=""):
    if vnev == "":
        print(f"{forma} {knev}!")
    else:
        print(f"{forma} {vnev} {knev}!")

koszon("Hello", "Béla", "Fazekas")
koszon(knev="János", forma="Szia", vnev="Nagy")
koszon("Szervusz", "Feri")
koszon("Csáó", "Marina")
koszon("Hola", "Dzsúlió")
