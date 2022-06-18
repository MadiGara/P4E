fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File not accessible", fname)
    exit()
wordic = dict()
largest = None

for line in fhand:
    line = line.rstrip()
    sline = line.split()
    if not line.startswith("From "): continue
    email = sline[1]
    wordic[email] = wordic.get(email,0) + 1
    #adds a count to the address key each loop

for value in wordic:
    #must use wordic[value] here, aka dictionary[iterationvar] or doesn't work
    #wordic[email] is already = 5 after above and anything else is not defined
    if largest is None or largest < wordic[value]:
        largest = wordic[value]
        largestname = value  
print(largestname, largest)
