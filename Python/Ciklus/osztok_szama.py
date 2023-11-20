# Pozitív egész osztók száma!
# 12 => 1 2 3 4 6 12 => 6
# 123456000 => 160

n = int(input("n: "))

# Megszámolás tétel
db = 0
for i in range(1, n+1):
    if n % i == 0:
        db += 1

print(f"Osztók száma: {db}")
