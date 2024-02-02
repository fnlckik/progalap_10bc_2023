from time import time

# UNIX-idő
# 1970. 01. 01
# Gond:
# Nem ugyanolyan a számok gyakorisága!
print(int(time()*100000) % 10)
