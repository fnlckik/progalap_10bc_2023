# Beolvasás
km = float(input("Kilométer: "))

# Feldolgozás
# 1 tm = 1852 km
# 1/1852 tm = 1 km
tm = km / 1852

# Kiírás
print("Tengeri mérföldben:", round(tm, 2))