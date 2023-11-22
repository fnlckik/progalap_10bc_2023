n = int(input("n: "))

eredmeny = 0
for i in range(1, n+1):
    aktualis = i*i
    if i % 2 == 0:
        eredmeny -= aktualis
    else:
        eredmeny += aktualis

print("Eredmény:", eredmeny)