n = int(input("n: "))

s = 0
for i in range(1, n+1):
    negyzet = i*i
    akt = 1 / negyzet
    s += akt

print(f"A kapott összeg: {round(s, 5)}")