# Be
n = int(input())
menetidok = []
for i in range(n):
    ido = int(input())
    menetidok.append(ido)

# Feld - Keresés
# i = 1
# while i < n and not(menetidok[i] < menetidok[i-1]):
#     i += 1
# if i < n:
#     print(i+1)
# else:
#     print(-1)

i = 0
while i < n-1 and not(menetidok[i+1] < menetidok[i]):
    i += 1
if i < n-1:
    print(i+2)
else:
    print(-1)
