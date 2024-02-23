# Sorok száma: 8
# X 0 X 0 X 0 X 0
# 0 X 0 X 0 X 0 X
# X 0 X 0 X 0 X 0
# 0 X 0 X 0 X 0 X
# X 0 X 0 X 0 X 0
# 0 X 0 X 0 X 0 X
# X 0 X 0 X 0 X 0
# 0 X 0 X 0 X 0 X

import os
from termcolor import colored

os.system("cls")

def sor(n, a, b):
    for i in range(n):
        if i % 2 == 0:
            print(colored(a, "red"), end=" ")
        else:
            print(colored(b, "green"), end=" ")
    print()
    
def sakktabla(n, a, b):
    for i in range(n):
        if i % 2 == 0:
            sor(n, a, b)
        else:
            sor(n, b, a)
    
def main():
    n = int(input("Sorok száma: "))
    sakktabla(n, "B", "W")
    
main()