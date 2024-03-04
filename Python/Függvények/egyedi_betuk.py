def eleme(e, h):
    i = 0
    while i < len(h) and not(h[i] == e):
        i += 1
    return i < len(h)

def egyedi_betuk(s):
    eredmeny = []
    for i in range(len(s)):
        if not eleme(s[i], eredmeny):
            eredmeny.append(s[i])
    return eredmeny

# list("monitor") == ["m", "o", "n", "i", "t", "o", "r"]
def main():
    print(egyedi_betuk("monitor"))
    print(egyedi_betuk("almafa"))
    print(egyedi_betuk("tolltartó"))

main()