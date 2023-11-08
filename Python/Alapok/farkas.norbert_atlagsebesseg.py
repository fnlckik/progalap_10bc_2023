v1 = float(input("1. sebesség: "))
v2 = float(input("2. sebesség: "))
t1 = int(input("1. idő: "))
t2 = int(input("2. idő: "))

s = v1*t1 + v2*t2
t = t1 + t2
v = s / t

print("Az átlagsebesség ", round(v, 2), "km/h.", sep="")
print("Az átlagsebesség " + str(round(v, 2)) + "km/h.")
print(f"Az átlagsebesség {round(v, 2)}km/h.")
