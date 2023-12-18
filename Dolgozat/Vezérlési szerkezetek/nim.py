kavics = 21

jatekos = "A"
print(f"A kupacban {kavics} kavics van.", end=" ")
while kavics > 0:
    x = int(input(f"{jatekos} játékos következik: "))
    kavics -= x
    if kavics <= 0:
        print(f"A kupacban 0 kavics maradt. Gratulálok {jatekos} játékosnak!")
    else:
        print(f"A kupacban {kavics} kavics maradt.", end=" ")

    if jatekos == "A":
        jatekos = "B"
    else:
        jatekos = "A"
