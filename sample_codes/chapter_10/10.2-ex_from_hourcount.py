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
    time = sline[5]
    parts = time.split(":")
    hour = parts[0]
    wordic[hour] = wordic.get(hour,0) + 1

#Sort dictionary by value
lst = list()
for hour, count in list(wordic.items()):
    lst.append((hour, count))
lst.sort()                   #sorts by ascending order by default
for hour, count in lst[:]:
    print(hour, count)
