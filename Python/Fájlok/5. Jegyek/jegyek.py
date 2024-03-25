from random import randint

def main():
    fw = open("jegyek.txt", "w", encoding="UTF-8")
    for i in range(17):
        r = randint(1, 5)
        # fw.write(str(r) + "\n")
        fw.write(f"{r}\n")
    fw.close()

main()