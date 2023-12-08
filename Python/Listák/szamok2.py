lista = [5, 3, 7, 4, 12, -9, 31, 7]
n = len(lista)

'''
5. Írasd ki a 3-mal osztható elemeket!
'''
# Kimenet:
# F5: 3 12 -9
print("F5:", end=" ")
for i in range(n):
    if lista[i] % 3 == 0:
        print(lista[i], end=" ")
print()


'''
6. Írasd ki az elemeket
fordított sorrendben!
'''
# Kimenet:
# F6: 7 31 -9 12 4 7 3 5
print("F6:", end=" ")
for i in range(n-1, -1, -1):
    print(lista[i], end=" ")
print()

# MO2
# print("F6:", end=" ")
# for i in range(n, 0, -1):
#     print(lista[i-1], end=" ")
# print()

# print("F6:", end=" ")
# for i in range(n):
#     print(lista[n-(i+1)], end=" ")
# print()

# Máté (python: negatív indexek)
# print("F6:", end=" ")
# for i in range(n):
#     print(lista[-(i+1)], end=" ")
# print()
