x = [1, 3, -4, 2, 6, 7]

y = []
for i in range(len(x)):
    if x[i] % 2 == 0:
        y.append(i)
print(y)

for i in range(len(y)):
    j = y[i] # y[i]: egy index az x listából
    print(x[j], end=" ")
