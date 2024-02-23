# Sorok száma: 8
# X 0 X 0 X 0 X 0
# 0 X 0 X 0 X 0 X
# X 0 X 0 X 0 X 0
# 0 X 0 X 0 X 0 X
# X 0 X 0 X 0 X 0
# 0 X 0 X 0 X 0 X
# X 0 X 0 X 0 X 0
# 0 X 0 X 0 X 0 X

def sor(n, a, b):
    for i in range(n):
        if i % 2 == 0:
            print(a, end=" ")
        else:
            print(b, end=" ")
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