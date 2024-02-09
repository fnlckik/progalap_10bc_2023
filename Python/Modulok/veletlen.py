from random import random

# Generáljunk egy random számot!
# [0; 1)
r = random()
print("[0, 1) random:", r)

# [0; 15) => [0; 1) * 15
r = random() * 15
print("[0, 15) random:", r)

# [0..5] = {0; 1; 2; 3; 4; 5}
# for i in range(40):
r = int(random() * 6)
print("[0..5] random:", r)

# [1..6] = {1; 2; 3; 4; 5; 6}
r = int(random() * 6) + 1
print("[1..6] random:", r)

# [13..19] = {13; 14; 15; 16; 17; 18; 19}
r = int(random() * 7) + 13
print("[13..19] random:", r)

# Általában!
# [a..b] = {a; a+1; ... ; b-1; b}
# hossz = b - a + 1
# kezdo = a
a = 8
b = 27
r = int(random() * (b - a + 1)) + a
print("[a..b] random:", r)