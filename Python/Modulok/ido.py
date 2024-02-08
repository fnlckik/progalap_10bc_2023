from time import time, sleep

# UNIX-idő
# 1970. 01. 01
# Gond:
# Nem ugyanolyan a számok gyakorisága!
# print(int(time()*100000) % 10)

for i in range(50):
    ido = time()
    # Magic...
    n = int(ido * 100000) % 10
    print(n, end=" ")
    sleep(0.000001)
