# Be
n = int(input())
homersekletek = []
for i in range(n):
    y = int(input())
    homersekletek.append(y)

# Feld - Max-kiv
# maxi: maximális elem indexe
# maxe: maximális elem értéke
maxi = 0
for i in range(1, n):
    if homersekletek[i] > homersekletek[maxi]:
        maxi = i

# Ki
print(maxi+1)
