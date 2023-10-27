#Beolvasás
ora = int(input("Óra: "))
perc = int(input("Perc: "))
masodperc = int(input("Másodperc: "))

# Feldolgozás
# 1 2 3 => 1*3600 + 2*60 + 3 => 3723
kimenet = ora * 3600 + perc * 60 + masodperc

# Kiírás
print(kimenet)
