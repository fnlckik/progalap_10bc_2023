# n! => 1*2*3*4*...*(n-1)*n
# 5! => 1*2*3*4*5 => 120
# 1! => 1
# 2! => 1*2 => 2
# 3! => 1*2*3 => 6
# 4! => 1*2*3*4 => 24
# 0! => 1

# Olvass be egy n poz. egész számot
# Írd ki n! értékét

# Beolvasás
n = int(input("n: "))

# Feldolgozás
# Mj: sorozatszámítás tétele
fakt = 1
for i in range(1, n+1):
    fakt = fakt * i

# fakt = 1
# i = 1
# while i < n+1:
#     fakt *= i
#     i += 1

# Kiírás
print(n, "faktoriális:", fakt)
