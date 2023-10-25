n = int(input("n: ")) #123

sz = n // 100 #1
ketjegyu = n % 100 #23
t = ketjegyu // 10 #2
e = ketjegyu % 10 #3

# szte => etsz
eredmeny = 100*e + 10*t + sz

print("Fordítva:", eredmeny)

