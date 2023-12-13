x = [6, 10, 3, 5, 2, 1, 12, 28]
# x[7] == 28

n = len(x)
for i in range(n):
    if x[i] % 2 == 0:
        print(x[i] // 2, end=" ")
