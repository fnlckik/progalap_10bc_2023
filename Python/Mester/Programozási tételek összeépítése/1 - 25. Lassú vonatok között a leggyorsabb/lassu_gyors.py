# Be
n = int(input())
menetidok = []
for i in range(n):
    x = int(input())
    menetidok.append(x)

# Feld. - Kiválogatás + Min-kiválasztás
# Válogassuk ki a 120 perc felettiek indexeit!
lassuak = []
for i in range(n):
    if menetidok[i] > 120:
        lassuak.append(i)
# print(lassuak)

# Kéne a legkisebb sebesség a lassú indexekhez tartozók közül!

if lassuak == []:
    print(-1)
else:
    mini = lassuak[0]
    for i in range(len(lassuak)):
        j = lassuak[i]
        if menetidok[j] < menetidok[mini]:
            mini = j
    print(mini+1, menetidok[mini])
    
