osztalyzat = int(input("Osztályzat: "))

# osztalyzat < 1 or osztalyzat > 20
# not (1 <= osztalyzat and osztalyzat <= 20)
# not (0 < osztalyzat and osztalyzat < 21)
# not (1 <= osztalyzat <= 20)
if not (1 <= osztalyzat and osztalyzat <= 20):
    print("Nem jó osztályzat!")
    exit()

if osztalyzat <= 10:
    print("Bukott!")
else:
    print("Nem bukott!")

print("Program vége!")