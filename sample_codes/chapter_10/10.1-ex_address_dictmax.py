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
    address = sline[1]
    wordic[address] = wordic.get(address,0) + 1
    #adds a count to the address key each loop

lst = list()
for email, count in list(wordic.items()):
    lst.append((count, email))
lst.sort(reverse = True)  #sorts by descending number of emails sent
for count, email in lst[:1]:
    print(email, count)
