def terulet(a, b=None):
    if b == None:
        b = a
    return a * b

# 3 és 7 oldalú téglalap terület
print("Téglalap:", terulet(3, 7)) 

# 6 oldalú négyzet terület
print("Négyzet:", terulet(6)) 