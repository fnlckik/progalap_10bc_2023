# positional argument: számít a sorrend
# keyword argument: kulcsszó alapján azonosít
# vnev="" => ez egy alapértelmezett értékadás
def koszon(forma, knev, vnev=""):
    if vnev != "":
        print(f"{forma} {vnev} {knev}!")
    else:
        print(f"{forma} {knev}!")
    
# 2 szabály:
# I. Meghívás: Positional argumentumok, utána keyword argumentumok
# II. Definíció: Non-default parameter, utána default parameter
    
koszon("Szia", "Béla", "Fazekas")
koszon(knev="János", vnev="Fekete", forma="Hello")
koszon(forma="Jó reggelt", knev="Eszter")
koszon("Csáó", "Károly")
koszon("Csáó", "Károly", vnev="Kovács")
