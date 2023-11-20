# Négyzetszámok n-ig
n = int(input("n: "))

i = 0
while i*i <= n:
    print(i*i, end=" ")
    i += 1

# i = 0
# aktualis = i*i
# while aktualis <= n:
#     print(aktualis, end=" ")
#     i += 1
#     aktualis = i*i

# for i in range(n):
#     if i*i <= n:
#         print(i*i, end=" ")