from random import randint

# Hanyadik dobás volt az első hatos?
# 3 1 5 5 6 => 5

dobas = randint(1, 6)
print(dobas, end=" ")
db = 1
while dobas != 6:
    dobas = randint(1, 6)
    print(dobas, end=" ")
    db += 1

print("\nDobások száma:", db)
