# Előfeltétel tesztelés
# 1 <= osztalyzat <= 5
# 0 < osztalyzat < 6

osztalyzat = int(input("Osztályzat: "))
jo = 0 < osztalyzat and osztalyzat < 6 # bool
while not jo:
    osztalyzat = int(input("Nem jó. Újra: "))
    jo = 0 < osztalyzat and osztalyzat < 6
