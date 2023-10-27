# Beolvasás
nap = int(input("Hét napja: "))

# Feldolgozás
if nap < 1 or nap > 7:
    print("Nem jó! A hét napja 1 és 7 között legyen!")
    exit()

# if nap == 1:
#     hetnapja = "Hétfő"
# else:
#     if nap == 2:
#         hetnapja = "Kedd"
#     else:
#         if nap == 3:
#             hetnapja = "Szerda"
#         else:
#             if nap == 4:
#                 hetnapja = "Csütörtök"
#             else:
#                 if nap == 5:
#                     hetnapja = "Péntek"
#                 else:
#                     hetnapja = "Hétvége"

if nap == 1:
    hetnapja = "Hétfő"
elif nap == 2:
    hetnapja = "Kedd"
elif nap == 3:
    hetnapja = "Szerda"
elif nap == 4:
    hetnapja = "Csütörtök"
elif nap == 5:
    hetnapja = "Péntek"
else:
    hetnapja = "Hétvége"

# Kiírás
print(hetnapja)