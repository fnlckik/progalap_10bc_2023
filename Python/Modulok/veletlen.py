from random import random

# random() => [0, 1) intervallumról random szám
# Kéne: 0 és 4 közötti!
# 5 fajta lehetőség
# for i in range(200):
#     r = int(random() * 5)
#     print(r, end=" ")

# Van: 0, 1, 2, 3, 4, 5
# Kéne: 13, 14, 15, 16, 17, 18
# for i in range(200):
#     r = int(random() * 6) + 13
#     print(r, end=" ")

# Kéne: [a, b] ~ [13, 18]
# hossz: b-(a-1) => b-a+1 ~ 18-13+1 => 6
# kezdes: a ~ 13

# Itt a recept!
# int(random() * hossz) + kezdes

# Pl.: [123, 322]
# hossz: 322-123+1 => 200
# kezdes: 123
for i in range(200):
    r = int(random() * (322-123+1)) + 123
    print(r, end=" ")
