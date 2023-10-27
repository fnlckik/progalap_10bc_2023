# Beolvasás
n = int(input("n: "))

# Feldolgozás
# 57 => 75
t = n // 10 #5
e = n % 10 #7
forditva = e * 10 + t

# Kiírás
print(e, t, sep="")
print(str(e) + str(t))
print(forditva)
