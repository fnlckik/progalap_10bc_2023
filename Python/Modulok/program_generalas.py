n = 120

for i in range(1, n+1):
    print(f"db{i} = 0")

print("if r == 1:")
print("    db1 += 1")
for i in range(2, n+1):
    print(f"elif r == {i}:")
    print(f"    db{i} += 1")

print("print(", end="")
for i in range(n-1):
    print(f"db{i+1}", end=", ")
print(f"db{n})")