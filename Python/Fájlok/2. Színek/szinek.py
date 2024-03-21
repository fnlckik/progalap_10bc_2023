def befajl(sz):
    fr = open("szinek.txt", "r")
    sz = fr.readlines()
    print(sz)
    fr.close()

def main():
    szinek = []
    befajl(szinek)
    print(szinek)

main()