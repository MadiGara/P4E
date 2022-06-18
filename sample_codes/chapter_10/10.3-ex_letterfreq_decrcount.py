fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File not accessible", fname)
    exit()
letdic = dict()
lst = list()

import string
# So can use string punctuation function to delete it later - Parsing
for line in fhand:
    line = line.rstrip()
    line = line.translate(str.maketrans('', '',string.punctuation))
    line = line.translate(str.maketrans('', '',string.digits))
    line = line.lower()
    words = line.split()

#To isolate by letter   
    for word in words:
        letters = list(word)
        for letter in letters:
            letdic[letter] = letdic.get(letter, 0) + 1

#To sort letters
countsort = list()
for letter, count in list(letdic.items()): #makes dictionary into list to sort
    countsort.append((count, letter))
countsort.sort(reverse = True)
for count, letter in countsort[:] :
    print(letter, count)
