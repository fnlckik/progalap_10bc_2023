from time import time, sleep

# UNIX idő: 1970. 01. 01
# Hány másodperc telt el azóta?
# print("Idő:", time())

# print("Random:", int(time()*10000) % 10)

for i in range(40):
    ido = time()
    # Magic...
    r = int(ido * 1000000) % 10
    # End magic
    print(r, end=" ")
    sleep(0.000001)
