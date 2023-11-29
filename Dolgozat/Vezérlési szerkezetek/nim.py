kupac = 21

jatekos = "A"
x = int(input(f"A kupacban {kupac} kavics van. {jatekos} játékos következik: "))
while kupac > 0:
    kupac -= x

    if kupac > 0:
        if jatekos == "A":
            jatekos = "B"
        else:
            jatekos = "A"
        x = int(input(f"A kupacban {kupac} kavics maradt. {jatekos} játékos következik: "))

print(f"A kupacban 0 kavics maradt. Gratulálok {jatekos} játékosnak!")
