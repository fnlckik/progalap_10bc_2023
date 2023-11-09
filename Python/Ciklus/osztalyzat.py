# Előfeltétel tesztelés
osztalyzat = int(input("Osztályzat: "))

'''
if 1 <= osztalyzat and osztalyzat <= 5:
    print("Jó!")
else:
    print("Nem jó!")
'''

jo = 1 <= osztalyzat and osztalyzat <= 5
while not jo:
    osztalyzat = int(input("Osztályzat: "))
    jo = 1 <= osztalyzat and osztalyzat <= 5

'''
while osztalyzat < 1 or osztalyzat > 5:
    osztalyzat = int(input("Osztályzat: "))
'''