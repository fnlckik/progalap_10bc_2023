from time import time

# UNIX idő: 1970. 01. 01
# Hány másodperc telt el azóta?
# print("Idő:", time())

print("Random:", int(time()*10000) % 10)
