x = [1, 5, 2, 3, 9, 7]
# x[4] == 9

n = len(x)
for i in range(n):
    if x[i] % 2 == 1:
        print(x[i]*x[i], end=" ")
