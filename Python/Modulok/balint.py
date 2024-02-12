s = ""
s += "if r == 1:\n    db1 += 1\n"
for i in range(2, 121):
	s += "elif r == " + str(i) + ":\n    db" + str(i) + " += 1\n"

print(s)
