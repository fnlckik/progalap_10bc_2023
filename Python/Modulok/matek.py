# import math => math.sqrt(2)
# import math as m => m.sqrt(2)
# from math import sqrt, factorial
from math import *

print("Gyök(2) =", round(sqrt(2), 3))
print("5! =", factorial(5))

# Kombináció
eredmeny = factorial(30) // (factorial(3) * factorial(27))
print("(30 alatt 3) =", comb(30, 3), eredmeny)

# Legnagyobb közös osztó - euklideszi algoritmus
# gcd: greatest common divisor
print("(20, 24) =", gcd(20, 24))

# Kör kerület: 2*r*pi
print("5 egység sugarú kör kerülete:", 2*5*pi)
