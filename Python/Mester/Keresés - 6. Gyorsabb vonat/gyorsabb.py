# Be
n = int(input())
menetidok = []
for i in range(n):
    x = int(input())
    menetidok.append(x)

# Feld. - Keresés
i = 1
while i < n and not(menetidok[i-1] > menetidok[i]):
    i += 1
    
# Ki
if i < n:
    print(i+1)
else:
    print(-1)