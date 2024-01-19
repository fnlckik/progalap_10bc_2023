# Be
n = int(input())
h = []
for i in range(n):
    be = int(input())
    h.append(be)

# Feld
maxi = 0
for i in range(1, n):
    if h[i] > h[maxi]:
        maxi = i

# Ki
print(maxi+1)
