fname = input("Enter a file name: ")
try:
    fhand = open(fname)
except:
    print("File not accessible", fname)
    exit()
wordic = dict()

for line in fhand:
    line = line.rstrip()
    sline = line.split()
    if not line.startswith("From "): continue
    day = sline[2]
    wordic[day] = wordic.get(day,0) + 1  #adds a count to the day key each loop
print(wordic)
