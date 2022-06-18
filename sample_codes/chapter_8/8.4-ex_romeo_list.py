fname = input("Enter file: ")
fhand = open(fname)
addhere = list()
for line in fhand:
    line = line.rstrip()
    srom = line.split()
    for word in srom:
        if word not in addhere:
            addhere.append(word)
addhere.sort()
print(addhere)
