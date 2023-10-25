# 57 => 75

# Beolvasás
n = int(input("n: "))

# Feld
e = n % 10 #7
t = n // 10 #5
# eredmeny = str(e) + str(t) # "75"
eredmeny = 10*e + t

# Kiírás
print("Fordítva:", eredmeny)
