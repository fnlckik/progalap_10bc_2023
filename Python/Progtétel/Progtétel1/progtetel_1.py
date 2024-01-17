x = [5, 1, -8, 2, 32, 12, 17, 32, -3, 5, 2]
n = len(x)

#-------------------------------------------------------------
# 1. A 4-gyel oszthatók száma => 4
db = 0
for i in range(n):
    if x[i] % 4 == 0:
        db += 1
print("1. A 4-gyel oszthatók száma:", db)

#-------------------------------------------------------------
# 2. A 10-nél kisebbek szorzata => 2400
szorzat = 1
for i in range(n):
    if x[i] < 10:
        szorzat *= x[i]
print("2. A 10-nél kisebbek szorzata:", szorzat)

#-------------------------------------------------------------
# 3. A legnagyobb szám (több esetén az első) sorszáma => 5
maxi = 0
for i in range(1, n):
    if x[maxi] < x[i]:
        maxi = i
print("3. A legnagyobb szám sorszáma:", maxi+1)

#-------------------------------------------------------------
# 4. Hány lokális maximum van? => 3
# Lokális maximum: nagyobb mindkét szomszédjánál
# Magyarázat: x[4] és x[7] és x[9] lokális maximumok

# x[i] szomszédai x[i-1] és x[i+1]
db = 0
for i in range(1, n-1):
    if x[i] > x[i-1] and x[i] > x[i+1]:
        db += 1
print("4. A lokális maximumok száma:", db)
