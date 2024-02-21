# Önhivatkozás
# Egy függvény / eljárás meghívja saját magát!

# Végtelen rekurzió
def f(n):
    print(n)
    f(n+1)
    
f(1)

# Végtelen ciklus
# n = 1
# while True:
#     print(n)
#     n += 1