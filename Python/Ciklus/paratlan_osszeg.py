# 7
# 1 + 3 + 5 + 7 = 16

# 18
# 1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 = 81

# Beolvasás
n = int(input("n: "))

# Feldolgozás (Zalán)
# osszeg = 0
# for i in range(n+1):
#     if i % 2 != 0:
#         osszeg += i     
        
# osszeg = 0
# for i in range(n+1):
#     if i % 2 == 1:
#         osszeg += i     
      
# (Máriusz)  
# osszeg = 0
# x = 1
# while x <= n:
#     osszeg += x
#     x += 2
        
# (Máté)
osszeg = 0
for i in range(1, n+1, 2):
    osszeg += i

# Kiírás
print("Páratlanok összege:", osszeg)
