elso = int(input("1. életkor: "))
masodik = int(input("2. életkor: "))

if elso >= 18 and masodik >= 18:
    print("Máris hozom amit kértek!")
elif elso >= 18:
    print("Csak a(z) " + str(elso) + " éves vendéget szolgálhatom ki!")
elif masodik >= 18:
    print("Csak a(z) " + str(masodik) + " éves vendéget szolgálhatom ki!")
else:
    print("Sajnos egyiküket sem szolgálhatom ki!")