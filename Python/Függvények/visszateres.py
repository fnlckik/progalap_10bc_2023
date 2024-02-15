# Másodfokú függvény
def f(x):
    print("Számolás!")
    return x*x

# Ez egy eljárás!
def e(x):
    # print(x*x)
    print(f(x))
    return None

# ----------------------------
#print(f(5)) # Számolás! 25
print(e(5)) # Számolás! 25 None

# Fv hívások sorrendje:
# print -> e -> print -> f -> print
# Verem: elsőként bekerülő = utoljára kikerülő
# Verem (stack): kicsi memória terület
# Pl.: itt vannak a függvényhívások