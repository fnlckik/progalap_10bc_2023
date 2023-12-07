# Adott egy egész számokból álló lista:
lista = [5, 3, 7, 4, 12, -9, 31, 7]
n = len(lista)

'''
1. Írasd ki a lista elemeit 
egymás mellé szóközzel elválasztva!
'''
# Kimenet:
# F1: 5 3 7 4 12 -9 31 7
print("F1:", end=" ")
for i in range(n):
    print(lista[i], end=" ")
print()

# MO2 (Alex) - foreach
# print("F1:", end=" ")
# for elem in lista:
#     print(elem, end=" ")
# print()

# MO3 (python)
# print("F1:", end=" ")
# print(*lista)

'''
2. Írasd ki az elemeket pontosvesszővel
és szóközzel elválasztva! Az utolsó
elem után ne legyen már pontosvessző!
'''
# Kimenet:
# F2: 5; 3; 7; 4; 12; -9; 31; 7
# print("F2:", end=" ")
# for i in range(n):
#     if i == n-1:
#         print(lista[i], end=" ")
#     else:
#         print(lista[i], end="; ")
# print()

# MO2 (Ricsi)
# print("F2:", end=" ")
# print(lista[0], end="")
# for i in range(1, n):
#     print(f"; {lista[i]}", end="")

# MO3 (Tamás)
print("F2:", end=" ")
for i in range(n-1):
    print(lista[i], end="; ")
print(lista[n-1])

# MO4 (python)
# print("F2:", end=" ")
# print(*lista, sep="; ")

'''
3. Írasd ki minden elem kétszeresét!
'''
# Kimenet:
# F3: 10 6 14 8 24 -18 62 14
print("F3:", end=" ")
for i in range(n):
    aktualis = lista[i]
    print(2*aktualis, end=" ")
print()

# MO2 (Bálint miau)
# print("F3:", end=" ")
# for miau in lista:
#     print(2*miau, end=" ")
# print()

'''
4. Írasd ki minden második elemet!
'''
# lista = [5, 3, 7, 4, 12, -9, 31, 7]
# Kimenet:
# F4: 3 4 -9 7
