# n => n!
# 5 => 5! = 120
# 8 => 8! = 40320

# Beolvasás
n = int(input("n: "))

# Feldolgozás
faktorialis = 1
for i in range(1, n+1):
    faktorialis = faktorialis * i
    print(faktorialis)

# Kiírás
print(f"{n}! = {faktorialis}")