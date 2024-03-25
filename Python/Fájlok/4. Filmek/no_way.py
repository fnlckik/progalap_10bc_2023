filereader = open("filmek.csv", "r")
contents = filereader.read()
contents = contents.split(sep="\n")
filmek = []
ratings= []
while True:
    break
lista = [ertete.split(sep=";") for ertete in contents]
lista.pop()
for e in lista:
    filmek.append(e[0])
    ratings.append(e[1])

atlag = sum(ratings) / len(ratings)
print("nemjo")

