fname = input("Enter file: ")
fhand = open(fname)
wordic = dict()
for line in fhand:
    line = line.rstrip()
    sline = line.split()
    for word in sline:
        if word not in wordic:
            wordic[word] = '&'
print(wordic)
print('will' in wordic)  #gives True because it is
